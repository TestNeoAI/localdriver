import asyncio
from playwright.async_api import async_playwright
import datetime
import os


# Utility function for logging and screenshots
async def log_error(page, error_message):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/error_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    await page.screenshot(path=screenshot_path)
    print(f"ERROR: {error_message}")
    print(f"Screenshot saved at: {screenshot_path}")


# Utility function for resilient clicks
async def click_with_fallback(page, selectors):
    for selector in selectors:
        try:
            await page.locator(selector).click(timeout=3000)
            return
        except Exception as e:
            print(f"Selector {selector} failed: {e}")
            continue
    raise Exception("None of the selectors worked.")


# Page Object Model (POM) for the OrangeHRM application
class OrangeHRMLoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"

    async def navigate_to_login(self):
        await self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    async def login(self, username, password):
        await self.page.locator(self.username_input).fill(username)
        await self.page.locator(self.password_input).fill(password)
        await click_with_fallback(self.page, [self.login_button])


class OrangeHRMDashboardPage:
    def __init__(self, page):
        self.page = page
        self.pim_menu = "a[href='/web/index.php/pim/viewPimModule']"
        self.employee_status_dropdown = "div[class*='oxd-select-text']"
        self.freelance_option = "div[role='option']:has-text('Freelance')"

    async def navigate_to_pim(self):
        await click_with_fallback(self.page, [self.pim_menu])

    async def filter_by_employee_status(self, status="Freelance"):
        await self.page.locator(self.employee_status_dropdown).click()
        await click_with_fallback(self.page, [self.freelance_option])


# Main Test Script
async def main():
    test_name = "Test OrangeHRM Login and PIM Filter"
    project_id = "project_123"
    nlp_id = "nlp_task_456"
    dom_snapshot_id = "dom_snapshot_789"

    print(f"Starting test: {test_name}")
    print(f"Metadata: project_id={project_id}, nlp_id={nlp_id}, dom_snapshot_id={dom_snapshot_id}")

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # Instantiate page objects
            login_page = OrangeHRMLoginPage(page)
            dashboard_page = OrangeHRMDashboardPage(page)

            # Step 1: Navigate to login page
            await login_page.navigate_to_login()

            # Step 2: Perform login
            await login_page.login(username="Admin", password="admin123")

            # Step 3: Navigate to PIM module
            await dashboard_page.navigate_to_pim()

            # Step 4: Filter by employee status
            await page.locator("div[class*='oxd-select-text']").filter(has_text="Freelance").click()

            print("Test completed successfully!")

        except Exception as e:
            await log_error(page, f"Test failed: {e}")
        finally:
            await browser.close()


# Run the test
if __name__ == "__main__":
    asyncio.run(main())
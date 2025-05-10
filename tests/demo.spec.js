const { test, expect } = require('@playwright/test');

test('Google search test', async ({ page }) => {
  await page.goto('https://www.google.com');
  await page.locator('textarea[name="q"]').fill('OpenAI');
  await page.keyboard.press('Enter');
  await expect(page).toHaveTitle(/OpenAI/i);
});

const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto('https://www.google.com');
  await page.locator('textarea[name="q"]').fill('OpenAI');
  await page.keyboard.press('Enter');
  await page.waitForTimeout(10000);  // Let user see something
  await browser.close();
})();

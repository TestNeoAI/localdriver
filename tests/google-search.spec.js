import { test, expect } from '@playwright/test';  
  
test('Google search test', async ({ page }) => {  
  // Navigate to Google  
  await page.goto('https://www.google.com');  
  
  // Verify the page title  
  await expect(page).toHaveTitle(/Google/);  
});  
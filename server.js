// File: local-agent/server.js

const express = require('express');
const { chromium } = require('playwright');
const cors = require('cors');

const app = express();
const PORT = 5005;

app.use(cors());
app.use(express.json());

app.post('/run', async (req, res) => {
  try {
    const browser = await chromium.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://www.saucedemo.com/');
    await page.locator('#user-name').fill('OpenAI');
 
    await page.waitForTimeout(5000); // wait to see the result
    await browser.close();

    res.json({ success: true, message: 'Playwright test completed.' });
  } catch (err) {
    console.error('Error running test:', err);
    res.status(500).json({ success: false, message: 'Test failed.', error: err.toString() });
  }
});

app.listen(PORT, () => {
  console.log(`Local Test Agent listening at http://localhost:${PORT}`);
});

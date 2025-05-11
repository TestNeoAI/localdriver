#!/bin/bash

cd /tests
npx playwright install
npx playwright test google-search.spec.js --headed --project=chromium

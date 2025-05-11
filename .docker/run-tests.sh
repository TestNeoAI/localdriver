#!/bin/bash

export DISPLAY=:1
cd /tests

# Install and ensure dependencies
npx playwright install

# Run test with Chromium flags to work inside Docker and be visible in Xvfb
npx playwright test google-search.spec.js --headed --project=chromium -- --launch-options='{"args":["--no-sandbox","--disable-dev-shm-usage"]}'

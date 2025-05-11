#!/bin/bash

export DISPLAY=:1  # Important for GUI display to show in VNC

# Optional: run a window manager like openbox (only once)
# openbox &

# Run Playwright test in headed mode
npx playwright test tests/google-search.spec.js --headed


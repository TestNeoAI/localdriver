#!/bin/bash
export DISPLAY=:1
npx playwright test /tests/google-search.spec.js --headed > /tmp/test.log 2>&1
cat /tmp/test.log

#!/bin/bash
export DISPLAY=:1
npx playwright test /tests/google-search.spec.js > /tmp/test.log 2>&1

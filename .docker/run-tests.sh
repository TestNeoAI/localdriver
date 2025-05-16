#!/bin/bash
export DISPLAY=:1
cd /tests
node google-search.spec.js > /tmp/test.log 2>&1

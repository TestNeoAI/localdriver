#!/bin/bash
export DISPLAY=:1
xterm &
sleep 300
node /tests/google-search.spec.js

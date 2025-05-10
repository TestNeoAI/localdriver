#!/bin/bash
Xvfb :99 -screen 0 1920x1080x16 &
export DISPLAY=:99

fluxbox &

# Start VNC server
x11vnc -display :99 -forever -passwd 1234 -shared &

# Start noVNC
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &
sleep 5

# Run your playwright test (sample)
npx playwright install
npx playwright test

# Keep container alive
tail -f /dev/null

#!/bin/bash

# Start Xvfb
echo "Starting Xvfb..."
Xvfb :1 -screen 0 1024x768x16 &
sleep 2

# Check if Xvfb started
if ! pgrep Xvfb > /dev/null; then
  echo "❌ Xvfb failed to start!"
  exit 1
else
  echo "✅ Xvfb started"
fi

# Set DISPLAY
export DISPLAY=:1

# Start window manager
fluxbox &

# Start VNC
x11vnc -display :1 -nopw -forever -shared &

# Start noVNC
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

# Start Flask server
python3 /server.py

#!/bin/bash

echo "🚀 Starting VNC-enabled Playwright container"

# Start Xvfb
echo "🎬 Starting Xvfb..."
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
echo "🧱 Starting Fluxbox..."
fluxbox &
sleep 2

# Start VNC server
echo "📡 Starting x11vnc..."
x11vnc -display :1 -nopw -forever -shared &
sleep 2

# Start noVNC
echo "🌐 Starting noVNC..."
/opt/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080 &
# OR: websockify --web=/opt/novnc 6080 localhost:5900 &

# Optional: Run Playwright test automatically (headful)
# npx playwright test --headed

# Start Flask backend
echo "🔧 Starting Flask server..."
python3 /server.py

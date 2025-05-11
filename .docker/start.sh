#!/bin/bash

# Start virtual display
Xvfb :1 -screen 0 1024x768x16 &
sleep 2  # Give Xvfb time to start

# Export DISPLAY
export DISPLAY=:1

# Start window manager
fluxbox &

# Start VNC server
x11vnc -display :1 -nopw -forever -shared &
sleep 2  # Let x11vnc bind to port 5900

# Start noVNC websockify (frontend on 6080)
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

# Start Flask app (do not background this)
python3 /server.py

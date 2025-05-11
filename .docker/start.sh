#!/bin/bash
set -e

# Start virtual display on :1
Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1

# Start lightweight window manager
fluxbox &

# Start VNC server without password, ensure it's bound to correct display and port 5900
x11vnc -display :1 -forever -nopw -rfbport 5900 &

# Start noVNC websockify, routing to the same port used by x11vnc
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

# Start the Flask server (this should be the main foreground process)
python3 /server.py

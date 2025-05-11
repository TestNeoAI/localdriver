#!/bin/bash

# Start virtual display
Xvfb :1 -screen 0 1024x768x16 &

# Start window manager
fluxbox &

# Start VNC server
x11vnc -forever -usepw -display :1 &

# Start noVNC with proper proxy
cd /usr/share/novnc
./utils/novnc_proxy --vnc localhost:5900 --listen 6080 &

# Start Flask server (DO NOT background this process)
python3 /server.py

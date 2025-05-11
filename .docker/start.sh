#!/bin/bash

# Start virtual display
Xvfb :1 -screen 0 1024x768x16 &

# Start window manager
fluxbox &

# Start VNC server
x11vnc -forever -usepw -display :1 &

# Start noVNC (websockify)
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

# Start Flask server (❌ DO NOT background this process)
python3 /server.py

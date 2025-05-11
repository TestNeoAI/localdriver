#!/bin/bash  
  
# Start the Fluxbox window manager  
fluxbox &  
  
# Start the Xvfb virtual display  
Xvfb :99 -screen 0 1920x1080x24 &  
  
# Start the VNC server  
x11vnc -display :99 -forever -nopw -listen 0.0.0.0 -rfbport 5900 &  
  
# Start the noVNC server  
websockify --web=/usr/share/novnc/ 6080 localhost:5900 &  
  
# Start the Flask server (if needed)  
python3 /server.py &  
  
# Keep the container running  
tail -f /dev/null  
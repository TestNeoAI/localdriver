# Base image with Playwright and X11 support  
FROM mcr.microsoft.com/playwright:v1.43.1-focal  
  
# Install additional packages (for VNC and noVNC support)  
RUN apt-get update && apt-get install -y \  
    fluxbox x11vnc xvfb novnc websockify curl wget python3 python3-pip \  
    && apt-get clean  
  
# Install Python dependencies for Flask  
RUN pip3 install flask flask_cors  
  
# Copy required scripts and test files  
COPY .docker/start.sh /start.sh  
COPY .docker/server.py /server.py  
COPY .docker/run-tests.sh /run-tests.sh  
COPY .docker/google-search.spec.js /google-search.spec.js

  
# Make scripts executable  
RUN chmod +x /start.sh /run-tests.sh  
  
# Expose VNC, noVNC, and Flask ports  
EXPOSE 5900 6080 6081  
  
# Start everything  
CMD ["/start.sh"]  
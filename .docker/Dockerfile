# Base image with Playwright and X11 support  
FROM mcr.microsoft.com/playwright:v1.43.1-focal

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    fluxbox \
    x11vnc \
    xvfb \
    curl \
    wget \
    python3 \
    python3-pip \
    git \
    net-tools \
    xterm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python Flask API dependencies
RUN pip3 install flask flask_cors

# Install Playwright for Node.js
# Set up working directory for Node
WORKDIR /playwright-setup

# Create package.json and install Playwright
RUN npm init -y && \
    npm install playwright && \
    npx playwright install



# Install noVNC + websockify manually
RUN git clone https://github.com/novnc/noVNC.git /opt/novnc && \
    git clone https://github.com/novnc/websockify /opt/novnc/utils/websockify

# Setup VNC password
RUN mkdir -p ~/.vnc && x11vnc -storepasswd 1234 ~/.vnc/passwd


# Copy application files
 
COPY .docker/start.sh /start.sh
COPY .docker/server.py /server.py
COPY .docker/run-tests.sh /run-tests.sh
COPY .docker/testrun.py /tests/testrun.py


# Make scripts executable
RUN chmod +x /start.sh /run-tests.sh

# Expose VNC (5900), noVNC (6080), Flask API (6081)
EXPOSE 5900 6080 6081

# Start services
CMD ["/start.sh"]

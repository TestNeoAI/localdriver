FROM mcr.microsoft.com/playwright:v1.43.1-focal

# Install dependencies
RUN apt-get update && apt-get install -y \
    fluxbox x11vnc xvfb novnc websockify wget curl python3 python3-pip \
    && mkdir ~/.vnc

# Set passwordless VNC
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

# Copy scripts
COPY .docker/start.sh /start.sh
COPY server.py /server.py
COPY run-tests.sh /run-tests.sh

RUN chmod +x /start.sh /run-tests.sh

# Install Flask
RUN pip3 install flask

EXPOSE 5900 6080 6081

CMD bash -c "/start.sh & python3 /server.py"

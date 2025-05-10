FROM mcr.microsoft.com/playwright:v1.43.1-focal

RUN apt-get update && apt-get install -y \
    fluxbox x11vnc xvfb novnc websockify wget curl \
    && mkdir ~/.vnc

# Set passwordless VNC
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

# Start script
COPY .docker/start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 5900 6080
CMD ["/start.sh"]

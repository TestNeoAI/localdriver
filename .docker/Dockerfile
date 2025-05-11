FROM mcr.microsoft.com/playwright:v1.43.1-focal

RUN apt-get update && apt-get install -y \
    fluxbox x11vnc xvfb novnc websockify wget curl python3 python3-pip \
    && mkdir ~/.vnc

RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

COPY .docker/start.sh /start.sh
COPY .docker/server.py /server.py
COPY .docker/run-tests.sh /run-tests.sh

RUN chmod +x /start.sh /run-tests.sh

RUN pip3 install flask flask-cors


EXPOSE 5900 6080 6081

CMD ["/start.sh"]

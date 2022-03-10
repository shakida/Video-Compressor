FROM debian:latest

RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN apt -qq update && apt -qq install -y git wget pv jq wget python3-dev ffmpeg mediainfo
RUN pip3 install -U -r requirements.txt
CMD ["bash","start.sh"]

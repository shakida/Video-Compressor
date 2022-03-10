FROM debian:latest

RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install -U pip
RUN apt -qq update && apt -qq install -y git wget pv jq wget python3-dev ffmpeg mediainfo
RUN pip3 install -U -r requirements.txt
CMD ["bash","start.sh"]

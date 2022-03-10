FROM debian:latest

RUN apt update && apt upgrade -y
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD ["bash","start.sh"]

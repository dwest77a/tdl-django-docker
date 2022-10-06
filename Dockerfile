# syntax=docker/dockerfile:1
FROM ubuntu:18.04

RUN apt update

RUN apt install python3 -y
RUN apt install python3-pip -y

CMD ['python','-m','pip','install','django','-y']

WORKDIR /app

COPY . /app

CMD ["python","app/manage.py","migrate"]
CMD ["python","app/manage.py","runserver"]

EXPOSE 8000
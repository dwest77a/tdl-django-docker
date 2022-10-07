# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver"]

EXPOSE 8000
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver"]
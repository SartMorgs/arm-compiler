FROM python:3.7

LABEL maintainer="Morgana Sartor <morgana.sartor@outlook.com>"

COPY ../requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ../. /app

CMD [ "python", "./api/api.py" ]
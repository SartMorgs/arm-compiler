FROM python:3.9

LABEL maintainer="Morgana Sartor <morgana.sartor@outlook.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /armcompiler

COPY ./requirements.txt /armcompiler/requirements.txt
RUN pip install --no-cache-dir -r /armcompiler/requirements.txt

ENV FLASK_APP armcompiler/api/api.py

WORKDIR /armcompiler

COPY . /armcompiler

EXPOSE 5000

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
FROM ubuntu:20.04

RUN apt update -y
RUN apt install python3-pip -y
RUN apt-get install -y python3-psycopg2

WORKDIR /app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


# install psycopg2


# install dependencies
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# add and run as non-root user
#RUN adduser -D suporte
#USER suporte
COPY . .
# running migrations
# RUN python manage.py migrate
RUN python3 manage.py collectstatic --noinput


# gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT

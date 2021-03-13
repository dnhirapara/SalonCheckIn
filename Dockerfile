FROM python:3.8-alpine

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/media
RUN mkdir $APP_HOME/static
RUN apk add zlib-dev jpeg-dev gcc musl-dev


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_HOME

RUN pip install --upgrade pip
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip install -r $APP_HOME/requirements.txt

COPY ./SalonCheckIn $APP_HOME
COPY ./entrypoint.sh $APP_HOME/entrypoint.sh

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
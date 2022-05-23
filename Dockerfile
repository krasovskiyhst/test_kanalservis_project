###########
# BUILDER #
###########

FROM python:3.10.2-alpine as builder

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установка зависимостей
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip

# проверка кода через линтер
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 /usr/src/test_kanalservis_project

# установка зависимостей
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/wheels -r requirements.txt


#########
# FINAL #
#########

FROM python:3.10.2-alpine

# создаем директорию для пользователя
RUN mkdir -p /home

# создаем отдельного пользователя
RUN addgroup -S app && adduser -S app -G app

# создание каталога для приложения
ENV HOME=/home
ENV APP_HOME=/home/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# установка зависимостей и копирование из builder
RUN apk update && apk add libpq
COPY --from=builder /usr/src/wheels /wheels
COPY --from=builder /usr/src/requirements.txt .
RUN pip install --no-cache /wheels/*

# копирование entrypoint-prod.sh
RUN chmod 774 ./entrypoint.prod.sh
COPY ./entrypoint.prod.sh $APP_HOME

# копирование проекта Django
COPY . $APP_HOME

# изменение прав для пользователя app
RUN chown -R app:app $APP_HOME

# изменение рабочего пользователя
USER app

ENTRYPOINT ["/home/web/entrypoint.prod.sh"]

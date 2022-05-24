# Тестовое задание для компании Каналсервис
Для развёртывания необходим сервер с предустановленным Docker

Ссылка на Гугл таблицу:\
https://docs.google.com/spreadsheets/d/1xxdwt6atoroNKWc0Ni6_vYc4-U1Cy4FT2d9HFTSjPnM/edit#gid=0

Установка на сервер
---------------------
*Если нет Git, устанавливаем:*\
**apt install git**

*Клонируем репозиторий:*\
**git clone https://github.com/krasovskiyhst/test_kanalservis_project.git**

*Переходим в папку с проектом*\
**cd test_kanalservis_project**

*Добавим файл с переменными виртуального окружения. В переменной "ALLOWED_HOSTS" нужно добавить IP сервера.*\
**sudo nano .env.prod**

    DEBUG=0
    SECRET_KEY=2shx%#&f4po*sr#q31=1+=p93-w(n((ofy-jc-^ev$@y#*55=5
    ALLOWED_HOSTS=localhost 127.0.0.1 [::1] <ЗАМЕНИТЬ НА IP СЕРВЕРА>

    POSTGRES_ENGINE=django.db.backends.postgresql_psycopg2
    POSTGRES_NAME=postgres
    POSTGRES_USER=test_kanalservis_user
    POSTGRES_PASSWORD=DVdh4nsn161zX0gv91ORjwtr4cLbY
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

Сохранить, закрыть.
**ctrl+o, Enter, ctrl+x**

*Запуск контейнеров*\
**docker-compose -f docker-compose.yml up -d --build**

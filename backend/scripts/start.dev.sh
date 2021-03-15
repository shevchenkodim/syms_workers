#!/bin/sh

if [[ "$DATABASE" = "postgres" ]]
then
    echo "Waiting for postgres..."

    while ! nc -z $DJANGO_SETTINGS_DATABASES_DEFAULT_HOST $DJANGO_SETTINGS_DATABASES_DEFAULT_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

rm ./*/migrations/0*.py
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
python manage.py create_custom_superuser
python manage.py runserver 0.0.0.0:8000

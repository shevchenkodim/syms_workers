#!/bin/sh

# check if Postgres is working before applying migrations and starting the Django development server
if [[ "$DATABASE" = "postgres" ]]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASES_HOST $DATABASES_PORT; do
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

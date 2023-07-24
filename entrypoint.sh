#!/bin/bash

set -e

echo "Collect static files"
python manage.py collectstatic --noinput

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput


gunicorn config.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=config.settings.dev \
    --name backend_django \
    --log-level=debug \
    --bind 0.0.0.0:8000 \
    --reload


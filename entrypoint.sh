#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput



gunicorn apps.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=apps.production_settings \
    --name apps \
    --bind 0.0.0.0:8001 \
    --timeout 600 \
    --workers 4 \
    --log-level=info \
    --reload
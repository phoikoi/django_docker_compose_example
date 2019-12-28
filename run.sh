#!/bin/bash
cd app
./manage.py migrate --noinput
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3

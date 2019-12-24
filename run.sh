#!/bin/bash
cd dcms
./manage.py migrate --noinput
exec gunicorn dcms.wsgi:application --bind 0.0.0.0:8000 --workers 3

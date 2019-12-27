#!/bin/bash
cd app
./manage.py migrate --noinput
exec ./manage.py runserver 0.0.0.0:8000

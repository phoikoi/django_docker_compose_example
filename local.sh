#!/bin/bash
cd dcms
./manage.py migrate --noinput
exec ./manage.py runserver 0.0.0.0:8000

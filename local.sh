#!/bin/bash
cd app

set -e

until PGPASSWORD=app psql -h db -U app -d app  -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

./manage.py migrate --noinput
exec ./manage.py runserver 0.0.0.0:8000

#!/bin/bash
pushd app
./manage.py collectstatic --noinput
popd
echo Starting nginx
/usr/sbin/nginx -c /code/prod-nginx.conf -g "daemon off;" >/dev/null 2>&1


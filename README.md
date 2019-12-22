# Django docker-compose template/bad example

This is an example of one way to use Django with docker-compose.  It
is probably not the best way.  You should definitely do your own
research on deployment methods before attempting to deploy a real site.
Your mileage may vary.  Offer not available in all states, subject to local
law.  Very slippery when wet.

At present, this repo uses Django-CMS as an example.  You can pretty easily replace
it with whatever Django-using application you want.

Before building the image, you should either copy or link to one of the .env
files, or create one of your own that has the same keys:

`ln -s prod.env .env` ... etc.

## The services

There are several services included in these compose files, but they differ slightly
between the local and the production version.

In the production version, the Django
main app listens on port `8057`, has `DEBUG` turned off (of course), and doesn't serve
static files.  The Nginx server listens on port `8058` and serves the static files (under
the `/static` subpath; it doesn't serve anything on the root path.)

In the local version, there is no Nginx server, and the Django app serves the static files
and has `DEBUG` enabled, as with a normal `runserver` command, which is exactly what it's running.

NOTE: the local top-level directory (where the dockerfiles, etc. are) is mapped to `/code` inside
the container in the local setup, and the Django app will auto-reload, so you can do your local
development with the container running.

NOTE 2: This example app doesn't handle the media files at all; you'll have to handle that, since
many people will want to use a CDN for those kinds of things, anyway.  (Hint: look at the
`django-storages` package if you want to use Django `FileField` with Amazon S3, etc.  This will
also work for the static files if you want to go that way, but you'll want to rearrange the way
that the `collectstatic` management command is run, or just ditch the nginx service entirely maybe.


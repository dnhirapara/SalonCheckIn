#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
echo "Done..."
exec "$@"
#!/bin/bash

echo "Apply database migrations"
python core/manage.py makemigrations && python core/manage.py migrate

echo "Create superuser"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD') if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() else print('Superuser already exists.')" | python core/manage.py shell

echo "Starting server"
python core/manage.py runserver 0.0.0.0:8000

exec "$@"

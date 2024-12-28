#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# Run Django migrations
python /code/app/manage.py migrate

VAR_NAME="ENVIRONMENT"

if [ -z "${!VAR_NAME:-}" ]; then
    # Environment variable does not exist, so create it with the value 'container'
    export ENVIRONMENT="container"
fi

if [ "${ENVIRONMENT}" == "local" ]; then
    echo "Starting Django development server"
    python /code/app/manage.py runserver 0.0.0.0:8000
else
    echo "Starting Gunicorn server"
    python /code/app/manage.py collectstatic --noinput
    gunicorn --forwarded-allow-ips="*" --pythonpath /code/app app.wsgi:application --workers=4 --bind 0.0.0.0:8000
fi

#!/usr/bin/env bash
set -o errexit
# Install dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

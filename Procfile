web: waitress-serve --port=$PORT --threads=$WEB_CONCURRENCY --channel-timeout=20 wow_tools.wsgi:application
release: python manage.py migrate

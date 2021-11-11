release: python manage.py migrate
web: gunicorn djangoProject.asgi:application -k uvicorn.workers.UvicornWorker
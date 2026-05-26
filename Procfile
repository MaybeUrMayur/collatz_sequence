web: python App/manage.py collectstatic --noinput && python App/manage.py migrate && gunicorn --chdir App backend.wsgi --bind 0.0.0.0:$PORT

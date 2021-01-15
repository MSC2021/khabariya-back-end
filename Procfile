release: python3 manage.py migrate
web:gunicorn khabri.wsgi --log-file -
web: python3 manage.py runserver 0.0.0.0:$PORT
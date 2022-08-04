FROM python:3.9
RUN pip install Flask uWSGI
WORKDIR /app
COPY app /app
CMD ["uwsgi", "--http", "0.0.0.0:8080", "--wsgi-file", "/app/app/main.py", \
    "--callable", "app", "--ini", "/app/uwsgi.ini"]
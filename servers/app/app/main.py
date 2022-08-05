import os
from time import sleep

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """Тестовый вебсервис"""
    return f'Server: {os.environ["APP"]}'


@app.route('/healthcheck')
def healthcheck():
    """Страница проверки доступности сервера"""
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

import os
# import logging
from flask import Flask

app = Flask(__name__)

# logger = logging.getLogger('serverLogger')
# fileHangler = logging.FileHandler(f'{os.environ["APP"]}_server.log')
# i = 0

@app.route('/')
def home():
    print(f'111111111111111111111111111111111')
    return f'Server: {os.environ["APP"]}'


@app.route('/healthcheck')
def healthcheck():
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

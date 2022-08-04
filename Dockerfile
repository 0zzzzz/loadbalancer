FROM python:3
RUN #pip install flask pyyaml
WORKDIR /usr/src/app
COPY ./app.py /app/app.py
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app
CMD ["python","-u", "/app/app.py"]

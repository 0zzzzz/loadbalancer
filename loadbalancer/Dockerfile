FROM python:3.9
WORKDIR /loadbalancer
COPY ./requirements.txt /loadbalancer/requirements.txt
RUN pip install -r /loadbalancer/requirements.txt
COPY . /loadbalancer
EXPOSE 5000
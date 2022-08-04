#FROM python:3
#RUN #pip install flask pyyaml
#COPY ./loadbalancer.py /loadbalancer/loadbalancer.py
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
CMD ["python","-u", "/loadbalancer/loadbalancer.py"]

#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

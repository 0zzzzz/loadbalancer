import requests
from flask import Flask, request
from utils import load_configuration, transform_backends_from_config, get_healthy_server
from tasks import healthcheck


loadbalancer = Flask(__name__)

config = load_configuration('loadbalancer.yaml')
register = transform_backends_from_config(config)



@loadbalancer.route('/')
def router():
    updated_register = healthcheck(register)
    for entry in config["hosts"]:
        healthy_server = get_healthy_server(entry["host"], updated_register)
        if not healthy_server:
            return "No Backends servers available", 503
        response = requests.get("http://{}".format(healthy_server.endpoint))
        return response.content, response.status_code
    return "Not Found", 404


if __name__ == '__main__':
    loadbalancer.run()

import requests
from flask import Flask
from utils import load_configuration, transform_backends_from_config, get_healthy_server, healthcheck


loadbalancer = Flask(__name__)

config = load_configuration('loadbalancer.yaml')
register = transform_backends_from_config(config)

@loadbalancer.route('/')
def router():
    """Распределитель нагрузки"""
    updated_register = healthcheck(register)
    for entry in config["hosts"]:
        print(entry)
        healthy_server = get_healthy_server(entry["host"], updated_register)
        print(healthy_server)
        if not healthy_server:
            return "Все серверы недоступны", 503
        response = requests.get("http://{}".format(healthy_server.endpoint))
        return response.content, response.status_code
    return "Страница не найдена", 404


if __name__ == '__main__':
    loadbalancer.run(host="0.0.0.0", debug=True)

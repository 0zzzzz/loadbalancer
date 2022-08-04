from models import Server
import yaml
import random


def load_configuration(path):
    """Загрузка конфигурации серверов"""
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config


def transform_backends_from_config(config):
    """Преобразовывает данные из конфигурации"""
    register = {}

    for entry in config.get('hosts', []):
        register.update({entry["host"]: [Server(endpoint) for endpoint in entry["servers"]]})
    print(f'1')
    print(config.get('hosts', []))
    print(f'2')
    print(register)
    return register


def get_healthy_server(host, register):
    """Случайный доступный сервер"""
    try:
        return random.choice([server for server in register[host] if server.healthy])
    except IndexError:
        return None


def healthcheck(register):
    """Проверка доступности сервера"""
    for host in register:
        for server in register[host]:
            server.healthcheck_and_update_status()
    return register

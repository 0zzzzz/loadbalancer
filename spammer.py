import requests


def spam(address):
    """Посылает зацикленные запросы на адресс"""
    while True:
        try:
            req = requests.get(address)
            print(f'SPAMMER TIME {req}')
        except:
            spam(address)


if __name__ == '__main__':
    spam('http://127.0.0.1:5000/')

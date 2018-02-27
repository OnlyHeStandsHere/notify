import requests


def get_users():
    url = 'http://localhost:5000/users/api/index'
    r = requests.get(url=url)
    print(r)
    print(r.json())


def get_clients():
    url = 'http://localhost:5000/clients/api/index'
    r = requests.get(url=url)
    print(r)
    print(r.json())



if __name__ == '__main__':
    get_clients()
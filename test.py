import requests
import json

URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def get_resource(id = None):
    data = {}
    if id is not None:
        data = {
            'id' : id,
        }

    resp = requests.get(URL+ENDPOINT , data = json.dumps(data))

    print(resp.status_code)
    print(resp.json())

# get_resource()

def create_resource():
    emp = {
        'eno':500,
        'ename':'Harish',
        'esal':4000,
        'eaddr':'Maysore'
    }
    resp = requests.post(URL+ENDPOINT, data = json.dumps(emp))

    print(resp.status_code)
    print(resp.json())

create_resource()

def update_resource(id):
    emp = {
        'id':id,
        'ename':'Sunny',
        'eno':400,
        'esal':45000
    }

    resp = requests.put(URL+ENDPOINT, data = json.dumps(emp))
    print(resp.status_code)
    print(resp.json())

# update_resource(1)

def delete_resource(id):

    emp = {
        'id':id
    }

    resp = requests.delete(URL+ENDPOINT, data=json.dumps(emp))
    print(resp.status_code)
    print(resp.json())

# delete_resource(9)

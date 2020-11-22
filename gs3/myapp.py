import requests 
import json

URL = "http://localhost:8000/studentapi/"


def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}

    r = requests.get(url=URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

# get_data()

def post_data(): # used to create data 
    data = {
        'name':'yash',
        'roll':200,
        'city':'faridabad',
    }

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}

    r = requests.post(url =URL,headers=headers, data = json_data)
    data = r.json()
    print(data) 

# post_data()
# get_data()

def update_data():
    data = {
        'id':2,
        'name':'gaurav',
        'city':'delhi',
    }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {'id':8}

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

# delete_data()
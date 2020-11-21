import requests 
import json

URL = "http://localhost:8000/stuinfo/"


def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data = json_data)
    data = r.json()
    print(data)
# when you want to get data 
# get_data(5)

def post_data(): # used to create data 
    data = {
        'name':'yash',
        'roll':200,
        'city':'faridabad',
    }

    json_data = json.dumps(data)

    r = requests.post(url =URL, data = json_data)
    data = r.json()
    print(data) 

#when you want to add data
post_data()

def update_data():
    data = {
        'id':5,
        'name':'gaurav',
        'city':'delhi',
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data() :
    data = {'id':8}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()

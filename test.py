import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+str(id)+'/')
    print(resp.json())
#get_resource(id)
def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.json())
#get_all():
def create_resource():
    new_emp={
    'eno':'6',
    'ename':'dhoni',
    'eLocation':'ranchi',
    'start_time':'2020-06-03 ',
    'end_time':'2020-06-24 ',

    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#create_resource()
def update_resource(id):
    new_emp={

    'eLocation':'Maharastra',
    'start_time':'2020-06-03 ',
    'end_time':'2020-06-24 ',

    }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#update_resource(1)
def delete_resource(id):
    resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(resp.status_code)
    print(resp.json())

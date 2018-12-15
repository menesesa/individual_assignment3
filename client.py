# -*- coding: utf-8 -*-

#%%
import requests

url = "http://127.0.0.1:5000"  

def get_contact(name):
   response = requests.get(url+"/contact/"+name)
   if response.status_code == 200:
       return response.json()
   else:
       return print(response.status_code)


def add_contact(name,phone):
    response = requests.post(url+"/add/"+name+"/"+phone)
    if response.status_code == 200:
        return response.json()
    else:
       return print(response.status_code)

def delete_contact(name):
    response = requests.post(url+"/delete/"+name)
    if response.status_code == 200:
        return response.json()
    else:
       return print(response.status_code)

def update_contact(name,number):
    response = requests.post(url+"/update/"+name+"/"+number)
    if response.status_code == 200:
        return response.json()
    else:
       return print(response.status_code)
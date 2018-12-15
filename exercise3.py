# -*- coding: utf-8 -*-

#%%
# Exercise 3


# 5 points. Create an HTTP server and HTTP client to manage a
# phonebook. There should exist the following operations in the phonebook:

# • add a contact (phone + name)
# • get a phone by name
# • delete a phone by name
# • update a phone by name

# Make sure you use JSON to communicate between client and server.

from flask import Flask, jsonify


phonebook = {"Robert": "7208628751", "Pedro": "303703876" }


server = Flask("PhoneBook server")

# get a phone by name   
@server.route("/contact/<name>")
def get_contact_phone(name):
    
    if name in phonebook :
        contact = phonebook[name]
        return jsonify(contact)
    else:
        return jsonify("Contact does not exist")
    
#add a contact (phone + name)
@server.route("/add/<name>/<phone>", methods=["POST"])    
def add_contact(name,phone):
    phonebook[name] = phone
    return jsonify({"Message":"Contact Added","Contact name":name,"Contact number":phone})

#delete a phone by name
@server.route("/delete/<name>", methods=["POST"])
def delete_number(name):
    phonebook.pop(name)
    return jsonify({"Message":"Contact deleted","Contact name":name})

#update a phone by name
@server.route("/update/<name>/<number>", methods=["POST"])
def update_number(name,number):
    phonebook[name] = number 
    return jsonify({"Message":"Contact number updated","Contact name":name,"Contact number":number})



server.run()            



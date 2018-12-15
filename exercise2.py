# -*- coding: utf-8 -*-
#%%

# Exercise 2


# 3 points. Using Github’s API, create a function that:
# • takes all repositories from your account
# • prints a short description of each repository, with its name, number
# of stars, main language, and url

import requests

def get_repo(username):
    
    url = "https://api.github.com/users/{}/repos".format(username)
    
    repository = requests.get(url).json()
    
    for rep in repository:
        print("Repository Name:{} \n Language:{} \n Stars:{} \n Url:{} \n".format(
                rep["name"],
                rep["language"],
                str(repository["stargazers_count"]),
                rep["url"]))
        
         
        
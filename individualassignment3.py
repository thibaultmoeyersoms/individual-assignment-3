
##exercise3
#%%
from flask import Flask, jsonify


phonebook = {
            "Thibault":"19586",
            "Bob":"23456",
            "Steven":"87657",
            "Alex":"54367"
             }

server = Flask("MyPhonebook")

@server.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)

@server.route("/addcontact/<name>/<phone_number>")
def add_contact(name,phone_number):
    new_contact = {name:phone_number}
    phonebook.update(new_contact)
    return jsonify(phonebook)

@server.route("/removecontact/<name>")
def remove_contact(name):
    phonebook.pop(name)
    return jsonify("Contact has been deleted!")

@server.route("/updatecontact/<name>/<phone>")
def update_contact(name,phone):
    phonebook [name] = phone
    return jsonify("Contact has been updated!")

@server.route("showphone/<name>")
def show_contact(name):
    contact = phonebook[name]
    return jsonify(contact)

server.run()

#%%

##exercise2

def get_repos(username):
    
    import requests

    url = "https://api.github.com/users/" + username + "/repos"
    response = requests.get(url)
    repos = response.json()
    
    repos_list = []
    
    for repo in repos :
        d = {"name":repo["name"],"stargazers_count": repo["stargazers_count"],"language":repo["language"]}
        repos_list.append(d)
        
    return repos_list
    
get_repos("thibaultmoeyersoms")

#%%






    



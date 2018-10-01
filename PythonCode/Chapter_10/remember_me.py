#!usr/bin/python
# -*- coding: utf-8 -*-
import json

"""
If username had been saved, load it.
Else, remind user enter name and save it.
"""

def get_stored_username():
    """
    If username had been saved, load it.
    """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username

def get_new_username():
    """
    Remind user enter name.
    """
    username = raw_input("What is your name? : ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """
    Greet user with username.
    """
    username = get_stored_username()
    if username:
        print "Welcome back, " + username + "!"
    else:
        username = get_new_username()
        print "We'll remember you when you come back, " + username + "!"

greet_user()


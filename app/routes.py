# from crypt import methods
from urllib import request
from flask import render_template
from app import app
import os

# global ls
# ls=[]

@app.route('/<string:content>', methods=['POST'])
def index(content):
    with open ("lb.txt", "a+") as f:
        f.write(content + "|")
    return f

@app.route('/')
def display():
    ls=[]
    try:
        with open ("lb.txt", "r") as f:
            content = f.read()
            ls.append(content.split("|"))
    except:
        pass
    return ls

if __name__ == "__main__":
    app.run()

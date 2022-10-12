# from crypt import methods
from urllib import request
from flask import render_template, Response
from app import app
import os, json

# global ls
# ls=[]

@app.route('/<string:content>', methods=['POST'])
def index(content):
    with open ("lb.txt", "a+") as f:
        f.write(content + "\n")
    return f

@app.route('/')
def display():
    ls=[]
    try:
        with open ("lb.txt", "r") as f:
            content = f.readlines()
            return render_template("index.html", lis=content)
    except:
        pass
    

if __name__ == "__main__":
    app.run()

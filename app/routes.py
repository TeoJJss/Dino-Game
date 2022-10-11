# from crypt import methods
from urllib import request
from flask import render_template
from app import app
import os, json

global ls
ls=[]

@app.route('/<string:content>', methods=['POST'])
def index(content):
    return ls.append(content)
ls=ls
@app.route('/')
def display():
    lis=sorted(ls, reverse=True)
    return json.dumps(lis)

if __name__ == "__main__":
    app.run()
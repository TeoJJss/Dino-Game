# from crypt import methods
from urllib import request
from flask import render_template
from app import app
import os

global ls
ls=[]

@app.route('/<string:content>', methods=['POST'])
def index(content):
    return ls.append(content)
ls=ls
@app.route('/')
def display():
    return ls

if __name__ == "__main__":
    app.run()
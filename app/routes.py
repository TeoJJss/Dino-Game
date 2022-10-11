# from crypt import methods
from urllib import request
from flask import render_template
from app import app
import os

global ls
ls=[]

@app.route('/<string:content>', methods=['POST'])
def index(content):
    return content

@app.route('/')
def display(content):
    return content





if __name__ == "__main__":
    app.run()
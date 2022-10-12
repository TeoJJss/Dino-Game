# from crypt import methods
import string
from urllib import request
from flask import render_template, Response
from app import app
import os, json, re

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
    file="lb.txt"

    lines = open(file).read().splitlines()
    splitted = (line.split(',') for line in lines)
    items = ((i[0], int(i[1])) for i in splitted)

    # Reversed sort
    reversed_items = sorted(items, key=lambda i: -i[1])

    with open (file, "w+") as f:
        for i in reversed_items:
            f.write(f"{i[0]},{i[1]}\n")
    # open(file, 'w+').write('\n'.join((f"\n{i[0]}, {i[1]}" for i in reversed_items)))
    # with open (file, "r") as f:
    #     for line in f:
    #         temp = line.split()
    #         for i in temp:
    #             ls.append(i)
    # with open(file, "w+") as f:
    #     for i in ls:
    #         f.writelines(i)
    #         f.writelines("\n")
    
    content=open(file).readlines()
    return render_template("index.html", lis=content)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

if __name__ == "__main__":
    app.run()

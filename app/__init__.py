from flask import Flask, render_template
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
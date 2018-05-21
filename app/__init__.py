from flask import Flask
from config import *

app = Flask(__name__)

from app import routes
from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'you will not pass'

from app import routes

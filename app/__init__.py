from flask import Flask, request, send_from_directory
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app,db)

from app import routes, models, errors
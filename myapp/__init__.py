from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# create DB instance:
db = SQLAlchemy(app)

from myapp.db_models import Resource

db.create_all()

from myapp import routes

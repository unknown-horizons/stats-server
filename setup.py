from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

DATABASE_URI = 'sqlite:////tmp/test.db'

DEBUG = True
SECRET_KEY = 'development key'

def create_app(name):
	# create our little application :)
	app = Flask(name)
	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
	app.config.from_object(__name__)
	app.config.from_envvar('FLASKR_SETTINGS', silent=True)
	return app
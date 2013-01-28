# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from setup import db, create_app
from models import Version, GameStart
from handlers.gamestart import GamestartHandler

app = create_app(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
	if request.json is not None:
		# TODO Handle this properly
		data = request.json
		GamestartHandler(data['gamestart'])
	else:
		abort(401)
	return redirect(url_for('show_gamestarts'))

@app.route('/')
def show_gamestarts():
	gamestarts = GameStart.query.all()
	return render_template('show_gamestarts.html', gamestarts=gamestarts)

# Run application
if __name__ == '__main__':
	db.app = app
	db.init_app(app)
	db.create_all()
	app.run()

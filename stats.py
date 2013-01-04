# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from setup import db, create_app
from models import Entry, Version, GameStart

app = create_app(__name__)

@app.route('/')
def show_entries():
	entries = Entry.query.all()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	entry = Entry(request.form['title'], request.form['text'])
	db.session.add(entry)
	db.session.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/upload', methods=['POST'])
def upload_data():
	if request.json is not None:
		# TODO Handle this properly
		data = request.json
		print data['gamestart']
		version = data['gamestart']['version']
		uuid = data['gamestart']['uuid']
		versions = Version.query.filter_by(version=version).all()
		new_version = None
		if len(versions) == 0:
			new_version = Version(version)
			db.session.add(new_version)
		else:
			new_version = versions[0]
		gamestart = GameStart(uuid, new_version)
		db.session.add(gamestart)
		db.session.commit()
	else:
		abort(401)
	return redirect(url_for('show_entries'))

@app.route('/gamestarts')
def show_gamestarts():
	gamestarts = GameStart.query.all()
	return render_template('show_gamestarts.html', gamestarts=gamestarts)

# Run application
if __name__ == '__main__':
	db.app = app
	db.init_app(app)
	db.create_all()
	app.run()
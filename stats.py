# all the imports
import sqlite3
import json
from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from sqlalchemy.sql import func
from setup import db, create_app
from models import Version, GameStart, OSInfo
from handlers.gamestart import GamestartHandler
from itertools import groupby


app = create_app(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
	if request.json is not None:
		data = request.json
		GamestartHandler(data['gamestart'])
	else:
		abort(401)
	return redirect(url_for('show_gamestarts'))

@app.route('/')
def show_gamestarts():
	gamestarts = GameStart.query.all()
	osinfos = OSInfo.query.all()
	osstats = []
	startstats = []
	for osinfo in osinfos:
		osstats.append([osinfo.system, len(osinfo.gamestarts)])
		entry = {'name': osinfo.system, 'data': []}
		for (dateinfo, gamestarts) in GameStart.get_grouped_by_day(osinfo.gamestarts):
			entry['data'].append([unix_time(datetime(*dateinfo)), len(list(gamestarts))])
		startstats.append(entry)
				
	return render_template('show_gamestarts.html', gamestarts=gamestarts, osstats=osstats, startstats=startstats)


def unix_time(dt):
	epoch = datetime.utcfromtimestamp(0)
	delta = dt - epoch
	return delta.total_seconds()*1000


# Run application
if __name__ == '__main__':
	db.app = app
	db.init_app(app)
	db.create_all()
	app.run()
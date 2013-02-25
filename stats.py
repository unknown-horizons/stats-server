# all the imports
import sqlite3
import json
from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from sqlalchemy.sql import func
from setup import db, create_app
from models import Version, GameStart, OSInfo, Uuid, MapStart, Map
from handlers.gamestart import GamestartHandler
from handlers.mapstart import MapstartHandler
from itertools import groupby


app = create_app(__name__)

handler_mapping = {
    GamestartHandler.HANDLE: GamestartHandler,
    MapstartHandler.HANDLE: MapstartHandler
}

@app.route('/upload', methods=['POST'])
def upload_data():
	if request.json is not None:
		data = request.json
		assert isinstance(data, dict) 
		if not 'uuid' in data:
			return
		uuid = Uuid.create_or_fetch(data['uuid'])
		for key, data in data.iteritems():
			if key in handler_mapping:
				handler_mapping[key](data, uuid)
	else:
		abort(401)
	return redirect(url_for('show_gamestarts'))

@app.route('/')
def show_gamestarts():
	gamestart_list = GameStart.query.all()
	osinfos = OSInfo.query.all()
	osstats = []
	startstats = []
	for osinfo in osinfos:
		osstats.append([osinfo.system, len(osinfo.gamestarts)])
		entry = {'name': osinfo.system, 'data': []}
		for (dateinfo, gamestarts) in GameStart.get_grouped_by_day(osinfo.gamestarts):
			entry['data'].append([unix_time(datetime(*dateinfo)), len(list(gamestarts))])
		startstats.append(entry)
				
	return render_template('show_gamestarts.html', gamestarts=gamestart_list, osstats=osstats, startstats=startstats)

@app.route('/mapstarts')
def show_mapstarts():
	mapstarts = MapStart.query.all()
	maps = Map.query.all()
	mapdata = {}
	for map in maps:
		mapdata[map.mapname] = len(map.mapstarts)
	mapdata = []
	for map in maps:
		mapdata.append([map.mapname, len(map.mapstarts)])
	return render_template('show_mapstarts.html', mapstarts=mapstarts, mapdata=mapdata)

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
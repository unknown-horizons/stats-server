from datetime import datetime
from itertools import groupby

from setup import db

class MapStart(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	uuid_id = db.Column(db.Integer, db.ForeignKey('uuid.uuid'))
	uuid = db.relationship("Uuid", backref=db.backref('mapstarts'))
	map_id = db.Column(db.String, db.ForeignKey('map.mapname'))
	mapname = db.relationship("Map", backref=db.backref('mapstarts'))
	
	def __init__(self, uuid, mapname):
		self.uuid = uuid
		self.mapname = Map.create_or_fetch(mapname)

	def __repr__(self):
		return '<MapStart %r>' % (self.mapname.mapname)
	
class Map(db.Model):
	mapname = db.Column(db.String(60), primary_key=True)
	
	def __init__(self, mapname):
		self.mapname = mapname

	def __repr__(self):
		return '<Map %r>' % (self.mapname)
	@classmethod
	
	def create_or_fetch(cls, mapname):
		maps = Map.query.filter_by(mapname=mapname).all()
		return_map = None
		if len(maps) == 0:
			return_map = Map(mapname)
			db.session.add(return_map)
		else:
			return_map = maps[0]
		return return_map
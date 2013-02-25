from datetime import datetime
from itertools import groupby

from setup import db

class MapStart(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	mapname = db.Column(db.String(60))
	uuid_id = db.Column(db.Integer, db.ForeignKey('uuid.uuid'))
	uuid = db.relationship("Uuid", backref=db.backref('mapstarts'))
	
	def __init__(self, uuid, mapname):
		self.uuid = uuid
		self.mapname = mapname

	def __repr__(self):
		return '<MapStart %r>' % (self.mapname)
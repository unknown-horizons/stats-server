from datetime import datetime
from itertools import groupby

from setup import db

class GameStart(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	uuid = db.Column(db.String(36))
	date = db.Column(db.DateTime())
	version_id = db.Column(db.Integer, db.ForeignKey('version.id'))
	version = db.relationship("Version", backref=db.backref('gamestarts'))
	osinfo_id = db.Column(db.Integer, db.ForeignKey('os_info.id'))
	osinfo = db.relationship("OSInfo", backref=db.backref('gamestarts'))
	
	def __init__(self, uuid, version, osinfo):
		self.uuid = uuid
		self.version = version
		self.date = datetime.now()
		self.osinfo = osinfo

	def __repr__(self):
		return '<GameStart %r %r>' % (self.date, self.version)
		
		
	@classmethod
	def get_grouped_by_day(cls, items):
		def grouper( item ): 
			return item.date.year, item.date.month, item.date.day
		return groupby(items, grouper)
			
		
from datetime import datetime

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

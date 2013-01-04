from datetime import datetime

from setup import db

class GameStart(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	uuid = db.Column(db.String(36), unique=True)
	date = db.Column(db.DateTime())
	version_id = db.Column(db.Integer, db.ForeignKey('version.id'))
	version = db.relationship("Version", backref=db.backref('gamestarts'))

	def __init__(self, uuid, version):
		self.uuid = uuid
		self.version = version
		self.date = datetime.now()

	def __repr__(self):
		return '<GameStart %r>' % self.title

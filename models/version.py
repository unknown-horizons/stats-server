from setup import db

class Version(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	version = db.Column(db.String(60), unique=True)

	def __init__(self, version):
		self.version = version

	def __repr__(self):
		return '<Version %r>' % self.version
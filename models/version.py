from setup import db

class Version(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	version = db.Column(db.String(60), unique=True)

	def __init__(self, version):
		self.version = version

	def __repr__(self):
		return '<Version %r>' % self.version		
	
	@classmethod
	def create_or_fetch(cls, version):
		versions = Version.query.filter_by(version=version).all()
		new_version = None
		if len(versions) == 0:
			new_version = Version(version)
			db.session.add(new_version)
		else:
			new_version = versions[0]
		return new_version
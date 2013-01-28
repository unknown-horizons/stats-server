from setup import db

class OSInfo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	system = db.Column(db.String(60))
	release = db.Column(db.String(60))

	def __init__(self, system, release):
		self.system = system
		self.release = release

	def __repr__(self):
		return '<OSInfo %r %r>' % (self.system, self.release)
	
	@classmethod
	def get_os_info(cls, system, release):
		osinfos = OSInfo.query.filter_by(system=system,release=release).all()
		osinfo = None
		if len(osinfos) == 0:
			osinfo = OSInfo(system, release)
			db.session.add(osinfo)
		else:
			osinfo = osinfos[0]
		return osinfo
		
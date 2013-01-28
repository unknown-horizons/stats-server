from models import Version, GameStart
from setup import db

class GamestartHandler(object):

	HANDLE = "gamestart"

	def __init__(self, data):
		version = data['version']
		uuid = data['uuid']
		versions = Version.query.filter_by(version=version).all()
		new_version = None
		if len(versions) == 0:
			new_version = Version(version)
			db.session.add(new_version)
		else:
			new_version = versions[0]
		gamestart = GameStart(uuid, new_version)
		db.session.add(gamestart)
		db.session.commit()

from models import Version, GameStart, OSInfo
from setup import db

class GamestartHandler(object):

	HANDLE = "gamestart"

	def __init__(self, data, uuid):
		print "Gamestart registered"
		version = data['version']
		new_version = Version.create_or_fetch(version)
		os_info = OSInfo.get_os_info(data['system'], data['release'])
		gamestart = GameStart(uuid, new_version, os_info)
		db.session.add(gamestart)
		db.session.commit()

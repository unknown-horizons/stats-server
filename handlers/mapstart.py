from models import MapStart
from setup import db

class MapstartHandler(object):

	HANDLE = "mapstart"

	def __init__(self, data, uuid):
		mapname = data['map']
		print "Recording mapstart:", mapname, uuid.uuid
		mapstart = MapStart(uuid, mapname)
		db.session.add(mapstart)
		db.session.commit()

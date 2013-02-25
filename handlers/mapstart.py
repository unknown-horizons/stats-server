from models import Version, GameStart, OSInfo
from setup import db

class MapstartHandler(object):

	HANDLE = "mapstart"

	def __init__(self, data, uuid):
		print data
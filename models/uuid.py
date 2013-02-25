from setup import db

class Uuid(db.Model):
	uuid = db.Column(db.String(36), primary_key=True)
	
	def __init__(self, uuid):
		self.uuid = uuid

	def __repr__(self):
		return '<UUID %r>' % (self.uuid)
	
	@classmethod
	def create_or_fetch(cls, uuid):
		uuids = Uuid.query.filter_by(uuid=uuid).all()
		return_uuid = None
		if len(uuids) == 0:
			return_uuid = Uuid(uuid)
			db.session.add(return_uuid)
		else:
			return_uuid = uuids[0]
		return return_uuid
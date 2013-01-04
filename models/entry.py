from setup import db

class Entry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), unique=True)
	text = db.Column(db.String(4000), unique=True)

	def __init__(self, title, text):
		self.title = title
		self.text = text

	def __repr__(self):
		return '<Entry %r>' % self.title

from app import db

class CAENCodeStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CAEN = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(400), unique=True)

    def __init__(self, CAEN, name):
        self.CAEN = CAEN
        self.name = name
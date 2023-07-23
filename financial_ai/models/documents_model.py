from financial_ai.models import db

class Documents(db.Model):
    __tablename__ = "Documents"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    document = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

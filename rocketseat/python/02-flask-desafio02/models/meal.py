from database import db

class Meal(db.Model):
    #id, name, description, datetime, is_diet
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    consumed_at = db.Column(db.String(80), nullable=False)
    on_diet = db.Column(db.Boolean, nullable=False)
from db_config import db

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(), unique=False, nullable=True)
    pdf_file = db.Column(db.String(), unique=False, nullable=False)
    questions_number = db.Column(db.Integer, nullable=False)
    questions_type = db.Column(db.String(), nullable=False)
    shared = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
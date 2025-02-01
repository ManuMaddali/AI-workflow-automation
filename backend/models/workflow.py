from backend import db
from datetime import datetime

class Workflow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    steps = db.Column(db.JSON, nullable=True)  # Ensure this field is present
    execution_logs = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # New field for prompt templates
    prompt_templates = db.Column(db.JSON, nullable=True)
    
    # Define relationship with User
    user = db.relationship('User', backref=db.backref('workflows', lazy=True))

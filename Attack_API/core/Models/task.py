from core.extensions import db

class Task(db.model):
    Task_id = db.Column(db.Integer, primary_key = True)
    agent = db.relationship("Agent")
    moment = db.Column(db.DateTime)
    retrieved = db.Column(db.Boolean)
    task_t
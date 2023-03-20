from core.extensions import db

class Result(db.Model):
    Key_id = db.Column(db.integer, primary_key = True)
    agent = db.relationship("Agent")
    key_type = db.Column(db.Integer)
    key = db.Column(db.String)
    registration_moment = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return "<Key(id='%s', agent_id=%s, type =%s, key=%s, registration moment = %s)>"%(str(self.Key_id), str(self.agent.Agent_id), str(self.key_type), self.key, self.registration_moment)
    
from core.extensions import db


class Agent(db.Model):
    Agent_id            = db.Column(db.Integer, primary_key=True)
    listener            = db.relationship("Listener")
    type                = db.Column(db.Integer)
    remote_ip           = db.Column(db.String(64))
    tasks               = db.relationship("Task")
    results             = db.relationship("Result")
    hostname            = db.Column(db.String(150))
    client_asym_key     = db.relationship("Key")
    listener_asym_key   = db.relationship("Key")
    listener_client_key = db.relationship("Key")
    last_seen           = db.Column(db.DateTime)
    sleept              = db.column(db.Integer)

    def __repr__(self) -> str:
        return f'<Agent id: "{self.Agent_id}", Listener: "{self.listener.listener_id}", agent type: "{self.type}", remote ip: "{self.remote_ip}", hostname: "{self.hostname}", last seen: "{self.last_seen}", current sleep time: "{self.sleept}">'






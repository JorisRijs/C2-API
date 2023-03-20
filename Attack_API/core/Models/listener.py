from core.extensions import db

class Listener(db.Model):
    Listener_id = db.Column(db.Integer, primary_key=True)
    port = db.Column(db.Integer)
    bind_ip = db.Column(db.String)
    running = db.Column(db.Boolean)
    public_key = db.relationship("Keys")
    private_key = db.relationship("Keys")
    symmetric_keys = db.relationship("Keys")

    def __repr__(self) -> str:
        return "<Listener(id=%s, port=%s, bind_ip=%s, running=%s)>"%(str(self.Listener_id), str(self.port), self.bind_ip, str(self.running))
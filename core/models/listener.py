from core.extensions import db

from sqlalchemy.dialects.postgresql import UUID
import uuid

# cryptography packages
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class Listener(db.Model):
    Listener_id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    port = db.Column(db.Integer)
    bind_ip = db.Column(db.String)
    running = db.Column(db.Boolean)
    public_key = db.relationship("Keys")
    private_key = db.relationship("Keys")
    symmetric_keys = db.relationship("Keys")

    def __init__(self, port, bind_ip):
        self.Listener_id = uuid.uuid4()
        self.port = port
        self.bind_ip = bind_ip
        

    def __repr__(self) -> str:
        return "<Listener(id=%s, port=%s, bind_ip=%s, running=%s)>"%(str(self.Listener_id), str(self.port), self.bind_ip, str(self.running))
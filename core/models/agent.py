import datetime
from core.extensions import db
from sqlalchemy.ext.hybrid import hybrid_property
from functions.db_helper import db_session
import uuid


class Agent(db.Model):
    id                  = db.Column(db.UUID(as_UUID=True), primary_key=True, default=uuid.uuid4)
    listener            = db.relationship("Listener")
    type                = db.Column(db.Integer)
    _remote_ip           = db.Column(db.String(64))
    tasks               = db.relationship("Task")
    results             = db.relationship("Result")
    _hostname            = db.Column(db.String(150))
    client_asym_key     = db.relationship("Key")
    listener_asym_key   = db.relationship("Key")
    listener_client_key = db.relationship("Key")
    last_seen           = db.Column(db.DateTime)
    _sleept              = db.column(db.Integer)

    def __init__(self, listener, type, sleept):
        self.Agent_ID = uuid.uuid4()
        self.listener = listener
        self.type = type
        self.sleept = sleept
    
    def __repr__(self) -> str:
        return f'<Agent id: "{self.Agent_id}", Listener: "{self.listener.listener_id}", agent type: "{self.type}", remote ip: "{self.remote_ip}", hostname: "{self.hostname}", last seen: "{self.last_seen}", current sleep time: "{self.sleept}">' 

    @property
    def agent_ID(self):
        return self.id

    @property
    def remote_ip(self):
        return self._remote_ip
    
    @_remote_ip.setter
    def set_remote_ip(self, ip):
        self._remote_ip = ip
    
    @property
    def hostname(self):
        return self._hostname
    
    @hostname.setter
    def set_hostname(self, hostname):
        self._hostname = hostname
    
    @property
    def sleept(self):
        return self._sleept
    
    @sleept.setter
    def set_sleept(self, interval):
        self._sleept = interval

    @property
    def last_seen(self):
        return self.last_seen

    @last_seen.setter
    def set_last_seen(self):
        self.last_seen = datetime.datetime.now()
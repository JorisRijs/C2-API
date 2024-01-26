from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from core.extensions import db
#from sqlalchemy.ext.declarative import declarative_base
from core.functions.db_helper import base
from sqlalchemy.orm import relationship
import sqlalchemy as sa
import datetime as dt

from core.exceptions.Model_exceptions import InvalidKeyType


# 0 = Symmetric private key
# 1 = asymmetric private key
# 2 = asymmetric public key
allowed_key_types = [0,1,2]

class Key(Base):
    id                      = Column(sa.Integer, primary_key = True)
    agent                   = relationship("Agent")
    key_type                = Column(sa.String)
    key                     = Column(sa.String)
    registration_moment     = Column(sa.DateTime)

    def __init__(self, key_id, agent, key_type, key):
        
        self.id                     = key_id
        self.agent                  = agent
        self.key                    = key
        self.key_type               = key_type
        self.registration_moment    = dt.datetime.utcnow()

    def __repr__(self) -> str:
        return "<Key(id='%s', agent_id=%s, type =%s, key=%s, registration moment = %s)>"%(str(self.Key_id), str(self.agent.Agent_id), str(self.key_type), self.key, self.registration_moment)

    @property
    def get_key_id(self):
        return self.id
    
    @property
    def get_key_type(self):
        return self.key_type
    
    @property
    def get_key_agent(self):

    @property
    def get_id(self):
        return self.id
    
    def validate_parameters(self, key_id, agent, key, key_type):
        # kldfnhkljrhn
        try:
            if key_type not in allowed_key_types:
                raise InvalidKeyType
            elif key[::3] != "AAAA" and key_type == 2:
                raise InvalidKeyType
            elif key[::2] != "b3B" and key_type == 1:
                raise InvalidKeyType
            elif key_type ==0 and (key[::3] == "AAAA" or key[::2] == b3B):
                raise InvalidKeyType 
        except InvalidKeyType:
            # lknkln
            print("test")

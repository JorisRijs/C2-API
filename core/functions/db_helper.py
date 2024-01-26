
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.attributes import set_attribute
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm.exc as sa_exc
import os

from models.agent import Agent
from models.key import Key
from models.listener import Listener
from models.result import Result
from models.task import Task

if not os.path.exists('../../DB'):
    os.mkdir('../../DB')
    engine = sqlalchemy.create_engine('sqllite///../../DB/app.db', echo=False, convert_unicode=True)
else:
    engine = sqlalchemy.create_engine('sqllite///app.db', echo=False, convert_unicode=True)
base = declarative_base()

db_session = scoped_session(sessionmaker(autocommit = False, autoflush=False, bind = engine))

def init_db():
    base.metadata.create_all(bind=engine)

def set_property(object_type, object_ID, attribute, value):
    try:
        obj = db_session.query(object_type).filter(object_type.id == object_ID).first()
        setattr(obj, attribute, value)
    except sa_exc.NoResultFound:
        return None
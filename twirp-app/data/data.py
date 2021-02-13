import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

# Need these imports in order to load all of the modules and link them to SQLAlchemy
from data.models import * 

_db_engine = create_engine(os.getenv("DATABASE_URL"), echo=False)
_session_factory = sessionmaker(bind=_db_engine)

ModelBase.metadata.create_all(_db_engine)

def getDbSession() -> Session:
    return _session_factory()

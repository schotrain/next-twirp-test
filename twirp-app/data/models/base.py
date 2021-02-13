from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import AbstractConcreteBase

ModelBase: AbstractConcreteBase = declarative_base()

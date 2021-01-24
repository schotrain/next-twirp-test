from data.models.base import ModelBase
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

class User(ModelBase):
     __tablename__ = 'users'

     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
     givenName = Column(String)
     familyName = Column(String)
     email = Column(String)
     imageUrl = Column(String)
     identityProviders = relationship("IdentityProviderUser", back_populates="user")


class IdentityProviderUser(ModelBase):
     __tablename__ = 'identity_provider_users'

     id = Column(Integer, Sequence('identity_provider_user_id_seq'), primary_key=True)
     provider = Column(String)
     provider_id = Column(String)
     user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
     user = relationship("User", back_populates="identityProviders")

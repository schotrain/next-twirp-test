from data.models.base import ModelBase
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship


class IdentityProviderUser(ModelBase):
    __tablename__ = "identity_provider_users"

    id: int = Column(
        Integer, Sequence("identity_provider_user_id_seq"), primary_key=True
    )
    provider: str = Column(String)
    provider_id: str = Column(String)
    user_id: int = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user: "User" = relationship("User", back_populates="identityProviderUsers")


class User(ModelBase):
    __tablename__ = "users"

    id: int = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    givenName: str = Column(String)
    familyName: str = Column(String)
    email: str = Column(String)
    imageUrl: str = Column(String)
    identityProviderUsers: list[IdentityProviderUser] = relationship(
        "IdentityProviderUser", back_populates="user"
    )

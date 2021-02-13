from data import models
from data.data import getDbSession
from sqlalchemy import and_

def save_user(user: models.User) -> None:
    db_session = getDbSession()
    db_session.save(user)


def get_user_from_idp_login(identity_provider: str, identity_provider_id: str) -> models.User:
    db_session = getDbSession()

    idp_user = db_session.query(models.IdentityProviderUser).filter(
        and_(
            models.IdentityProviderUser.provider == identity_provider,
            models.IdentityProviderUser.provider_id == identity_provider_id
        )).first()

    return idp_user
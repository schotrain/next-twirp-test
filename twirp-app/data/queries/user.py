from data import models
from sqlalchemy import and_
from sqlalchemy.orm.session import Session


def find_identity_provider_user(
    db_session: Session, identity_provider: str, identity_provider_id: str
) -> models.User:
    idp_user = (
        db_session.query(models.IdentityProviderUser)
        .filter(
            and_(
                models.IdentityProviderUser.provider == identity_provider,
                models.IdentityProviderUser.provider_id == identity_provider_id,
            )
        )
        .first()
    )
    return idp_user
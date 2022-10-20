from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, EmbeddedField, ListField, BoolField, DateField


def roles_validator(roles):
    allowable_roles = [
        'Guest',
        'Player',
        'Administrator',
        'NannyModerator',
        'RegularModerator',
        'SeniorModerator',
    ]
    for role in roles:
        if role not in allowable_roles:
            raise ValueError(f'Role {role} should be from list {allowable_roles}')


class Rating(Base):
    enabled = BoolField()
    quality = IntField()
    quantity = IntField()


class User(Base):
    login = StringField()
    roles = ListField(str, validators=[roles_validator])
    medium_picture_url = StringField(name='mediumPictureUrl')
    small_picture_url = StringField(name='smallPictureUrl')
    status = StringField()
    rating = EmbeddedField(Rating)
    online = DateField()
    name = StringField()
    location = StringField()
    registration = DateField()


class UserEnvelopeResponseModel(Base):
    resource = EmbeddedField(User)
    metadata = StringField()

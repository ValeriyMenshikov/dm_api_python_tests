from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, EmbeddedField, ListField, BoolField, DateField


class PagingSettings(Base):
    posts_per_page = IntField(name='postsPerPage')
    comments_per_page = IntField(name='commentsPerPage')
    topics_per_page = IntField(name='topicsPerPage')
    messages_per_page = IntField(name='messagesPerPage')
    entities_per_page = IntField(name='entitiesPerPage')


class UserSettings(Base):
    # TODO сделать валидатор для списка доступных тем [ Modern, Pale, Classic, ClassicPale, Night ]
    color_schema = StringField(name='colorSchema')
    nanny_greetings_message = StringField(name='nannyGreetingsMessage')
    paging = EmbeddedField(PagingSettings)


class InfoDbText(Base):
    value = StringField()
    # TODO сделать валидатор для списка доступных режимов [ Common, Info, Post, Chat ]
    parse_mode = StringField(name='parseMode')


class Rating(Base):
    enabled = BoolField()
    quality = IntField()
    quantity = IntField()


class UserDetails(Base):
    login = StringField()
    # TODO сделать валидатор для списка доступных ролей [ Guest, Player, Administrator, NannyModerator, RegularModerator, SeniorModerator ]
    roles = ListField(str)
    medium_picture_url = StringField(name='mediumPictureUrl')
    small_picture_url = StringField(name='smallPictureUrl')
    status = StringField()
    rating = EmbeddedField(Rating)
    online = DateField()
    name = StringField()
    location = StringField()
    registration = DateField()
    icq = StringField()
    skype = StringField()
    original_picture_url = StringField(name='originalPictureUrl')
    info = EmbeddedField([InfoDbText, str])
    settings = EmbeddedField(UserSettings)


class UserDetailsEnvelopeResponseModel(Base):
    resource = EmbeddedField(UserDetails, required=True)
    metadata = StringField()

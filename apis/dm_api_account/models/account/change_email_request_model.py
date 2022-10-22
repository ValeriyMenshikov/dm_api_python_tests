from jsonmodels.models import Base
from jsonmodels.fields import StringField


class ChangeEmailRequestModel(Base):
    login = StringField()
    password = StringField()
    email = StringField()

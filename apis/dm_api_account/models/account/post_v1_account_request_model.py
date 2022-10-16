from jsonmodels.models import Base
from jsonmodels.fields import StringField


class RegistrationRequestModel(Base):
    login = StringField()
    email = StringField()
    password = StringField()

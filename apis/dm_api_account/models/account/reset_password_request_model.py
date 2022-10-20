from jsonmodels.models import Base
from jsonmodels.fields import StringField


class ResetPasswordRequestModel(Base):
    login = StringField()
    email = StringField()
from jsonmodels.models import Base
from jsonmodels.fields import StringField


class GeneralErrorResponseModel(Base):
    message = StringField()

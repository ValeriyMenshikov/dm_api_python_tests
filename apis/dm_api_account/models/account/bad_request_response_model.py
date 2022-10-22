from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, EmbeddedField, ListField, BoolField, DateField


class BadRequestResponseModel(Base):
    message = StringField()
    invalid_properties = EmbeddedField(ListField(str))

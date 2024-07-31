from datetime import datetime as dt
from apiflask import Schema
from apiflask.fields import String, Boolean, Integer, DateTime
from apiflask.validators import Length


class UserIn(Schema):
    username: str = String(required=True)
    password: str = String(
        required=True,
        validate=[
            Length(min=6, error="A senha não pode conter menos de 6 caracteres.")
        ],
    )


class UserOut(Schema):
    id: int = Integer()
    username: str = String()
    admin: bool = Boolean()
    active: bool = Boolean()
    created_at: dt = DateTime()

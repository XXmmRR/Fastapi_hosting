import ormar
from db import metadata, database
import datetime
from typing import Optional


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=25)
    email: str = ormar.String(max_length=100)
    password: str = ormar.String(max_length=100)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)


class Video(ormar.Model):
    class Meta(MainMeta):
        tablename = "videos"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=50)
    description: str = ormar.String(max_length=500)
    path: str = ormar.String(max_length=1000)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Optional[User] = ormar.ForeignKey(User)

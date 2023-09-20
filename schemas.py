from pydantic import BaseModel
from typing import List


class UploadVideo(BaseModel):
    title: str
    description: str


class User(BaseModel):
    id: int
    password: str


class GetVideo(BaseModel):
    user: User
    title: str
    description: str

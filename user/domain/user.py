# coding=utf-8

from dataclasses import dataclass
from datetime import datetime


# @dataclass
# class Profile :
#     name: str
#     email: str


@dataclass
class User:
    id : str
    name : str
    email : str
    password : str
    memo: str | None
    created_at : datetime
    updated_at : datetime


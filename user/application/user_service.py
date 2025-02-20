# coding=utf-8
from ulid import ULID
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository
from fastapi import HTTPException, Depends
from typing import Annotated

from dependency_injector.wiring import inject, Provide
from containers import Container


class UserService:
    @inject
    def __init__(
            self,
            user_repo: IUserRepository,
            ):
        self.user_repo = user_repo
        self.ulid = ULID()

    def create_user(self, name: str, email: str, password: str):
        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=password,
            created_at=now,
            updated_at=now,
            )
        self.user_repo.save(user)
        return user

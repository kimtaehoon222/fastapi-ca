# coding=utf-8
from ulid import ULID
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository
from fastapi import HTTPException, Depends
from typing import Annotated

from dependency_injector.wiring import inject, Provide



class UserService:
    @inject
    def __init__(
            self,
            user_repo: IUserRepository,
            ):
        self.user_repo = user_repo
        self.ulid = ULID()

    def create_user(self, name: str, email: str, password: str, memo: str | None = None, ):
        now = datetime.now()
        user: User = User(
            id=self.ulid.generate(),
            name=name,
            email=email,
            password=password,
            memo=memo,
            created_at=now,
            updated_at=now,
            )
        self.user_repo.save(user)
        return user

    def update_user(self, user_id: str, name: str | None = None, password: str | None = None,):
        user = self.user_repo.find_by_id(user_id)

        if name:
            user.name = name
        if password:
            user.password = self.crypto.encrypt(password)

        user.updated_at = datetime.now()

        self.user_repo.update(user)

        return user

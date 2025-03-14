# coding=utf-8
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from dependency_injector.wiring import inject, Provide
from containers import Container

from user.application.user_service import UserService

router = APIRouter(prefix="/users")


class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str


@router.post("", status_code=201)
@inject
def create_user(
        user: CreateUserBody,
        user_service: UserService = Depends(Provide[Container.user_service]),
        # user_service: Annotated[UserService, Depends(UserService)],
        ):
    # 이렇게 매번 인스턴스를 새로 만들지 않고 의존성 주입으로 만듦
    # user_service = UserService()
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password

        )

    return created_user


class UpdateUser(BaseModel):
    name: str | None = None
    password: str | None = None


@router.put("/{user_id}")
@inject
def update_user(user_id: str, user: UpdateUser, user_service: UserService = Depends(Provide[Container.user_service])):
    user = user_service.update_user(
            user_id= user_id,
            name= user.name,
            password= user.password,
        )

    return user
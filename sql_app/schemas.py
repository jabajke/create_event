from typing import List, Optional

from pydantic import BaseModel


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    member_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class AssociationBase(BaseModel):
    extra_data: str


class AssociationCreate(AssociationBase):
    pass


class Association(AssociationBase):
    left_id: int
    right_id: int

    class Config:
        orm_mode = True

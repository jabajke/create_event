from typing import List, Optional

from pydantic import BaseModel


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    events: List[Event] = []

    class Config:
        orm_mode = True

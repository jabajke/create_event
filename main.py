import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

con = sqlite3.connect('sqlitedb.sqlite3')

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserOut(BaseModel):
    """ В респонс нельзя передавать пароль,
     делаем UserOut без пароля и передаем в респонс """
    username: str
    email: EmailStr


class Event(BaseModel):
    event_name: str
    event_description: str
    event_time: Optional[datetime] = datetime.now()


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.post("/event/", response_model=Event)
async def create_event(event: Event):
    return event

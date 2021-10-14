from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
from typing import Optional

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
    date_in_7_days = datetime.now() + timedelta(days=7)
    event_title: str
    event_description: str
    event_time: Optional[datetime] = datetime(year=date_in_7_days.year, month=date_in_7_days.month,
                                              day=date_in_7_days.day, hour=18)


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.post("/event/", response_model=Event)
async def create_event(event: Event):
    return event




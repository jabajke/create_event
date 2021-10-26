from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already registered")
    return crud.create_user(db=db, user=user)


@app.get('/users/', response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get('/users/{user_id}')
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_db = crud.get_user(db, user_id=user_id)
    if user_db is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user_db


@app.get('/users/{left_id}/events/', response_model=List[schemas.Association])
def get_event_for_user(left_id: int, db: Session = Depends(get_db)):
    user = crud.get_association(db, left_id=left_id)
    return user


@app.post('/events/', response_model=schemas.Event)
def create_event(user_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    if crud.get_user(db, user_id=user_id).is_admin:
        db_event = crud.create_event(db, item=event, user_id=user_id)
    return db_event


@app.get('/events/', response_model=List[schemas.Event])
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events


@app.post('/events/sign/', response_model=schemas.Association)
def sign_on_event(left_id: int, right_id: int, association: schemas.AssociationCreate,
                  db: Session = Depends(get_db)):
    db_association = crud.create_association(db, item=association, left_id=left_id, right_id=right_id)
    return db_association

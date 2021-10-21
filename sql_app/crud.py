from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    not_hashed_password = user.password + "not hashed"
    db_user = models.User(username=user.username, hashed_password=not_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def create_event(db: Session, item: schemas.EventCreate, user_id: int):
    db_event = models.Event(**item.dict(), member_id=user_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_association(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Association).offset(skip).limit(limit).all()


def create_association(db: Session, item: schemas.AssociationCreate, left_id: int, right_id: int):
    db_association = models.Association(**item.dict(), left_id=left_id, right_id=right_id)
    db.add(db_association)
    db.commit()
    db.refresh(db_association)
    return db_association

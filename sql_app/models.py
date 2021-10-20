from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

# association_table = Table('association', Base.metadata,
#                           Column('users_id', ForeignKey('users.id'), primary_key=True),
#                           Column('events_id', ForeignKey('events_id'), primary_key=True)
#                           )


class Association(Base):
    __tablename__ = 'association'
    left_id = Column(ForeignKey('users.id'), primary_key=True)
    right_id = Column(ForeignKey('events.id'), primary_key=True)
    extra_data = Column(String(50))
    events = relationship('Event', back_populates='users')
    users = relationship('User', back_populates='events')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    events = relationship('Association', back_populates='users')


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    member_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("Association", back_populates="events")

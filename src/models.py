import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


class User(Base):
    __tablename__ = 'user'
    id = Column(int, primary_key=True)
    username = Column(str(80))
    password = Column(str(250))
    email = Column(str(250))
    favorites = Column(int, ForeignKey('favorites.object_id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    object_id = Column(int, ForeignKey('characters.id', 'planets.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(int, primary_key=True)
    gender = Column(str(250))
    hair_color = Column(str(250))
    eye_color = Column(str(250))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(int, primary_key=True)
    population = Column(str(250))
    terrain = Column(str(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
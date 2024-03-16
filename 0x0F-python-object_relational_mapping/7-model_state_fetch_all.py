#!/usr/bin/python3

"""
lists all states objects from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
import urllib.parse

username = urllib.parse.quote(argv[1])
password = urllib.parse.quote(argv[2])
database = urllib.parse.quote(argv[3])

engine = create_engine(
    'mysql://{}:{}@localhost:3306/{}'
    .format(username, password, database)
    )

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

all_states = session.query(State).order_by(State.id).all()

for obj in all_states:
    print("{}: {}".format(obj.id, obj.name))

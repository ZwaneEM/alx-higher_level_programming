#!/usr/bin/python3

"""
lists all states objects from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
import urllib.parse

if __name__ == "__main__":

    username = urllib.parse.quote(argv[1])
    password = urllib.parse.quote(argv[2])
    database = urllib.parse.quote(argv[3])
    state_name = "Louisiana"

    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'
        .format(username, password, database)
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()

    print(new_state.id)

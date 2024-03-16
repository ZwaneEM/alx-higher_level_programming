#!/usr/bin/python3

"""
lists all states objects from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv
import urllib.parse

if __name__ == "__main__":

    username = urllib.parse.quote(argv[1])
    password = urllib.parse.quote(argv[2])
    database = urllib.parse.quote(argv[3])
    state_name = "New Mexico"

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    state = session.query(State).all()

    city = session.query(text("City")).filter_by(state_id=state.id).all()


for state in session.query(State).all():
    city = session.query(text("City")).filter_by(state_id=state.id).all()
    print(city.name)
    

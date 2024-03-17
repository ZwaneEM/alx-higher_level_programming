#!/usr/bin/python3

"""
Prints the State object with the name passed
as argument
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    engine = create_engine("mysql://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == stateName).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

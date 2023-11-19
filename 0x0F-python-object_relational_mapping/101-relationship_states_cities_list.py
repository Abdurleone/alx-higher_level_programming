#!/usr/bin/python3

"""
Module to connect python script to database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":

    """Establish db connection"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    my_session_maker = sessionmaker(bind=engine)
    my_session = my_session_maker()

    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for City in state.cities:
            print("     {}: {}".format(City.id, City.name))

    my_session.close()

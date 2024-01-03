#!/usr/bin/python3

"""
Module to connect python script to database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    """Establish db connection"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    my_session_maker = sessionmaker(bind=engine)
    my_session = my_session_maker()

    state = my_session.query(State).filter_by(id=2).first()
    state.name = "New Mwxico"
    my_session.commit()

    my_session.close()

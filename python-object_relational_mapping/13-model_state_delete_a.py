#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()
    for line in session.query(State).filter(State.name.like('a')):
        session.delete(line)
    session.commit()
    session.close()

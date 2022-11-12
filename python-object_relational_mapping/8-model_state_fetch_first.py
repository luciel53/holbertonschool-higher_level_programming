#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa
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

    line = session.query(State).first()

    if line:
        print("{}: {}".format(line.id, line.name))
    else:
        print("Nothing")

    session.close()

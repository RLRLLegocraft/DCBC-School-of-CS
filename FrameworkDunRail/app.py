from volunteer import Volunteer
from train import Train, Carriage, StationMaster
import sqlite3
from uuid import uuid4
################################################################################
"""
It makes sense to have the event class in the main area
What we need to do is:
-take in how many customers there are
-organise a train using the StationMaster that fits everyone
-distribute volunteers in the carriages of that train
Obviously, we also need to link the volunteers and the carriages in the database.
"""

class Event(object):
    def __init__(self, customers, date, description=""):
        self.id = str(uuid4())[:8]
        self.customers = customers
        self.date = date
        self.description = description
        self.train = Train(customers)


################################################################################

if __name__ == '__main__':

    #CREATE db
    conn = sqlite3.connect('TEST.db')
    c = conn.cursor()
    c.execute("""CREATE TABlE IF NOT EXISTS Tester (
    name1 varchar2 Primary Key,
    name2 varchar2,
    score numeric
    )""")
    #c.execute("INSERT INTO Tester VALUES ('Sam','Mia', 50000)")
    conn.commit()

    #CREATE Sarah and her Carriage sets
    sarah = StationMaster()

    #CREATE Volunteer Table and addVolunteer method
    #CREATE EVENTS TABlE

    def createEvent(customers, date, description=""):
        e = Event(customers, date, description)
        #make some condition so no two events have the same id
""""
        while(True):
            try:
                query = "CREATE TABlE IF NOT EXISTS {} (name1 varchar2 Primary Key, name2 varchar2, score numeric)".format(e.id)
                c.execute(query)
                break
            except sqlite3.OperationalError as error:
                print("We are here: {}".format(error))
                continue
""""


        #INSERT Event details
        #CREATE *eventID*Volunteers Table

        #1.FOR EVERY Volunteer in *eventID*Volunteers Table
        #2. SEND e.description to volunteer.email
    createEvent(300, 2018, "Yeah the bois.")

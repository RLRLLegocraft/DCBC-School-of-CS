import uuid
"""
Here is probably the most important class.

"""
class Volunteer(object):

    #creates and assigns random id to volunteer
    def __init__(self, first, last):
        self.id = uuid.uuid4()
        self.first = first
        self.last = last

    def add_phone(self, phone):
        self.phone = phone


################################################################################

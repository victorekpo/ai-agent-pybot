import uuid
from datetime import datetime


class Machine:
    chron_counter = 0  # Class variable to keep track of the chronological ID

    def __init__(self, name):
        Machine.chron_counter += 1
        self.id = uuid.uuid4()
        self.chronId = Machine.chron_counter
        self.name = name
        self.dob = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

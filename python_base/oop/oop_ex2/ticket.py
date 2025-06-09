import datetime
import random


class Ticket:
    START_ID = 1
    END_ID = 100000
    FORMATTED_DATE = '%Y.%-m.%-d %H:%M:%S'

    def __init__(self, question):
        self.id = random.randint(self.START_ID, self.END_ID)
        self.question = question
        self.date = datetime.datetime.now().strftime(self.FORMATTED_DATE)

    def __str__(self):
        return f'{self.question}'

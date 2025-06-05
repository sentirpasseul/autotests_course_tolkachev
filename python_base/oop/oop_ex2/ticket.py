import datetime
import random

class Ticket:
    def __init__(self, question):
        self.id = random.randint(1, 100000)
        self.question = question
        self.date = datetime.datetime.now().strftime('%Y.%-m.%-d %H:%M:%S')
    def __str__(self):
        return f'{self.question}'





import random

class Ticket:
    def __init__(self, question):
        self.id = random.randint(1, 100000)
        self.question = question

    def __str__(self):
        return f'{self.id}. {self.question} {self.date}'



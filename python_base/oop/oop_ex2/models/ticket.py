import datetime


class Ticket:
    _id = 1
    FORMATTED_DATE = '%Y.%-m.%-d %H:%M:%S'

    def __init__(self, question):
        self.id = Ticket._id
        Ticket._id += 1
        self.question = question
        self.date = datetime.datetime.now().strftime(self.FORMATTED_DATE)

    def __str__(self):
        return f'{self.question}'

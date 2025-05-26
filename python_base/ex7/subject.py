from faker_base import FakerBase


class Subject:

    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def __str__(self):
        return f'{self.name}'

import random


class Human:
    MIN_AGE = 18
    MAX_AGE = 60
    _id = 1

    def __init__(self, name: str, age: int):
        self._id = Human._id
        Human._id += 1
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    @classmethod
    def reply(cls):
        return input()

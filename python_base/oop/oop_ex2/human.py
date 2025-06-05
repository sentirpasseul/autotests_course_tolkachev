import random


class Human:
    MIN_ID = 1
    MAX_ID = 10000
    MIN_AGE = 18
    MAX_AGE = 60

    def __init__(self, name: str, age: int):
        self.id = random.randint(self.MIN_ID, self.MAX_ID)
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    @staticmethod
    def reply():
        return input()

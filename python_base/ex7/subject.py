from faker import Faker


class Subject:
    MIN_HOURS = 10
    MAX_HOURS = 80

    def __init__(self, name):
        self.name = name
        self.hours = Faker().random_int(min=self.MIN_HOURS, max=self.MAX_HOURS)

    def __str__(self):
        return f'{self.name}'

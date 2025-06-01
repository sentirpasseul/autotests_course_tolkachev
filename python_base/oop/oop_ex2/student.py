import random

from human import Human


class Student(Human):
    def __init__(self, name: str, age: int, avg_score: float):
        super().__init__(name=name, age=age)
        self.id = random.randint(1, 10000)
        self.avg_score = avg_score

    def __str__(self):
        return f'{self.name} {self.age} {self.gender} {self.avg_score}'

    def learn(self):
        pass

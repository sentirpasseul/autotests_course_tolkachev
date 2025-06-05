import random

from human import Human


class Student(Human):
    def __init__(self, name: str, age: int, avg_score: float, exam_score=0):
        super().__init__(name=name, age=age)
        self.avg_score = avg_score
        self.exam_score = exam_score

    def __str__(self):
        return f'{self.name} {self.age} {self.avg_score}'

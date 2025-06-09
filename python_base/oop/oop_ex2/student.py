import random

from human import Human


class Student(Human):
    _id_student = 1

    def __init__(self, name: str, age: int, avg_score: float, exam_score=0):
        super().__init__(name=name, age=age)
        self.id = Student._id_student
        Student._id_student += 1
        self.avg_score = avg_score
        self.exam_score = exam_score

    def __str__(self):
        return f'{self.name} {self.age} {self.avg_score}'

from student import Student
from teacher import Teacher


class Assistant(Teacher, Student):
    def __init__(self, name: str, student_name: str, grade: str):
        Teacher.__init__(self, name)
        Student.__init__(self, student_name)

        self.teacher = name
        self.student = student_name
        self.grade = grade

    def __str__(self):
        return f'у студента {self.student} группы {self.grade} куратор {self.teacher}'

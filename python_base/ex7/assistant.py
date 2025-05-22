from student import Student
from teacher import Teacher


class Assistant(Teacher, Student):
    def __init__(self, teacher_name: str, student_name: str, grade: str):
        super().__init__(student_name)

        self.teacher = teacher_name
        self.student = student_name
        self.grade = grade

    def __str__(self):
        return f'у студента {self.student} группы {self.grade} куратор {self.teacher}'

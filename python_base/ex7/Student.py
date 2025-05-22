class Student:
    def __init__(self, student_name: str):
        self.name = student_name

    def __str__(self):
        return self.name

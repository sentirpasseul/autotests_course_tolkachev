from student import Student


class Teacher:
    SPARE_TIME = 140

    def __init__(self, name):
        # self.subject = subject
        # self.student = student
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def take_time(hours):
        return Teacher.SPARE_TIME - hours

    def teach(self):
        return f'{self.name} преподает у '

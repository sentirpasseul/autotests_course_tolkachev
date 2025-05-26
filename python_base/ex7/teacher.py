from person import Person


class Teacher(Person):
    SPARE_TIME = 140

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_time(hours):
        return Teacher.SPARE_TIME - hours

    def teach_student(self, student_name):
        return f'{self.name} преподает у {student_name}'

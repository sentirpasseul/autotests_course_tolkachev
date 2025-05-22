from student import Student


class Teacher:
    SPARE_TIME = 140

    def __init__(self, teacher_name):
        # self.subject = subject
        # self.student = student
        self.name = teacher_name

    def print_free_time(self):
        return self.SPARE_TIME

    def __str__(self):
        return self.name

    """
    def teach_student(self):
        spare_time = self.take_time(self.subject.hours)
        result = (f"{self.print_free_time()}, часов свободного времени у преподавателя\n"
                  f"Преподаватель {self.student.name} обучает {self.subject.name} {self.student}\n"
                  f"Предмет берет на себя {self.subject.hours} часов\n"
                  f"У преподавателя остается {spare_time} часов\n")
        return result
    
    """

    def print_hours_subject(self):
        return self.subject.hours

    def take_time(self, hours):
        return self.SPARE_TIME - hours

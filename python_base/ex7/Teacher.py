from Student import Student


class Teacher:
    def __init__(self, subject, student, teacher_name: str):
        self.subject = subject
        self.student = student
        self.teacher_name = teacher_name
        self.teacher_spare_time = 140

    def print_free_time(self):
        return self.teacher_spare_time

    def teach_student(self):
        spare_time = self.take_time(self.subject.hours_subject)
        print(self.print_free_time(), 'часов свободного времени у преподавателя')
        print(f'Преподаватель {self.teacher_name} обучает {self.subject.name_subject} студента {self.student.student_name}')
        print(f'Преподаватель {self.teacher_name} обучает {self.subject.name_subject} студента {self.student}'
              f'\nПредмет берет на себя {self.subject.hours_subject} часов')
        print(f'У преподавателя остается {spare_time} часов')

    def print_hours_subject(self):
        return self.subject_hours

    def take_time(self, hours):
        return self.teacher_spare_time - hours

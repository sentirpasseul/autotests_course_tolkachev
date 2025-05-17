from Student import Student
from Subject import Subject
from Teacher import Teacher


class Schedule:
    def __init__(self, student_name, teacher_name, subject_name, subject_hours):
        self.subject = Subject(subject_name, subject_hours)

        self.student = Student(student_name)
        self.student = student_name

        self.teacher_geography = Teacher(teacher_name=teacher_name, subject=self.subject, student=self.student)


    def take_time(self):
        self.teacher_geography.teach_student()


schedule = Schedule(teacher_name='Андрей Прокопьев', student_name='Евдокимов Дмитрий', subject_name='География',
                    subject_hours=20).take_time()

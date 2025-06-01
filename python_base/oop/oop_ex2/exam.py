import datetime
import random

from ticket_generator import TicketGenerator
from subject import Subject
from teacher import Teacher
from student import Student
from student_group import StudentGroup
from faker import Faker


class Exam:
    def __init__(self):
        self.faker = Faker()
        self.student_group = StudentGroup(grade='1', qualification=self.faker.job())
        self.teacher = Teacher(self.faker.name_male(), self.faker.random_int(min=18, max=60), self.faker.job())
        self.subject = Subject(self.faker.job())
        self.ticket_generator = TicketGenerator()
        self.statuses = ['passed', 'canceled', 'in progress', 'not passed']
        self.time_now = None
        self.time_end = None

    def get_student_group(self, number: int):
        for _ in range(number):
            name = self.faker.name()
            age = self.faker.random_int(min=18, max=37)
            avg_score = round(random.uniform(2.0, 5.0), 2)
            student = Student(name=name, age=age, avg_score=avg_score)
            self.student_group.add_student_in_group(student)
        return self.student_group.students

    def start(self, seconds):
        self.time_now = datetime.datetime.now()
        self.time_end = datetime.timedelta(seconds=seconds) + self.time_now
        print(self.get_ticket())
        print(self.get_text_start_exam())
        print(self.get_student_group(5))
        while self.time_now < self.time_end:
            self.time_now = datetime.datetime.now()
        print(self.get_text_end_exam())

    def get_text_start_exam(self):
        return f'Экзамен начался в {self.time_now.strftime('%H:%M:%S')}'

    def get_text_end_exam(self):
        return f'Экзамен закончился в {self.time_end.strftime('%H:%M:%S')}'

    def get_ticket(self):
        return f'Предмет: {self.subject} \n' \
               f'Преподаватель: {self.teacher.name} \n'


exam = Exam()
exam.start(3)

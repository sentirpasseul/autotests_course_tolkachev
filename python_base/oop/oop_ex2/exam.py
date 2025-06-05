import datetime
import random

from ticket_generator import TicketGenerator
from subject import Subject
from teacher import Teacher
from student import Student
from student_group import StudentGroup
from faker import Faker
from exam_status import ExamStatus


class Exam:
    def __init__(self, student_group, teacher, subject, difficulty):
        self.faker = Faker()
        self.student_group = student_group
        self.teacher = teacher
        self.subject = subject
        self.student = Student
        self.ticket_generator = TicketGenerator(difficulty=difficulty, quantity=2, subject=self.subject)
        self.statuses = list(ExamStatus)
        self.time_now = None
        self.time_end = None
        self.notify_students_about_exam()
        self.teacher_reply = ''
        self.student_answer = ''
        self.answer = ''

    def start(self, seconds):
        self.time_now = datetime.datetime.now()
        self.time_end = datetime.timedelta(seconds=seconds) + self.time_now
        print(self.get_ticket())
        print(self.get_text_start_exam())
        while self.time_now < self.time_end:
            self.time_now = datetime.datetime.now()
            self.student_answer = self.student.reply()
            self.teacher_reply = self.teacher.reply()
            self.answer = self.check_answer()
            if self.teacher_reply != '':
                break

            print(self.time_now)
        print(self.get_result_exam(self.answer))
        print(self.get_text_end_exam())

    def notify_students_about_exam(self):
        return f'Уважаемые студенты группы {self.student_group.number} {self.student_group.qualification}!\n' \
               f'Скоро начнется экзамен! Пожалуйста, уберите электронные приборы в рюкзак и сдайте зачетную книжку {self.teacher.name}'

    def get_text_start_exam(self):
        return f'Экзамен начался в {self.time_now.strftime('%H:%M:%S')}'

    def get_text_end_exam(self):
        return f'Экзамен закончился в {self.time_end.strftime('%H:%M:%S')}'

    def get_ticket(self):
        for ticket in self.ticket_generator:
            return f'Предмет: {self.subject} \n' \
                   f'Преподаватель: {self.teacher.name} \n' \
                   f'Группа: {self.student_group.number} \n' \
                   f'Вопрос: {ticket}'

    def check_answer(self):
        if self.teacher_reply.lower() == 'да' or self.teacher_reply.lower() == 'yes':
            return 'passed'
        else:
            return 'failed'

    def get_result_exam(self, status):
        result = ''
        for value in self.statuses:
            if value == status:
                result = value
        match result:
            case 'passed':
                return 'Экзамен сдан. Поздравляем!'
            case 'failed':
                return 'Экзамен провален.'

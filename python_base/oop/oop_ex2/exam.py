import datetime
import random
from enum import StrEnum, Enum

from ticket_generator import TicketGenerator
from subject import Subject
from teacher import Teacher
from student import Student
from student_group import StudentGroup
from exam_statuses import ExamStatuses
from answers import Answers


class Exam:
    FORMATTED_TIME = '%H:%M:%S'
    EXAM_SUCCESS = 'Экзамен сдан. Поздравляем!'
    EXAM_FAILED = 'Экзамен провален.'

    def __init__(self, student_group, teacher, subject, difficulty):
        self.__student_group = student_group
        self.__teacher = teacher
        self.__subject = subject
        self.__ticket_generator = TicketGenerator(difficulty=difficulty, quantity=2).get_ticket()
        self.__statuses = ExamStatuses
        self._answers = Answers
        self.time_now = None
        self.time_end = None
        self.notify_students_about_exam()
        self.teacher_reply = ''
        self.student_answer = ''
        self.answer = ''

    def start(self, seconds):
        self.time_now = datetime.datetime.now()
        self.time_end = datetime.timedelta(seconds=seconds) + self.time_now
        print(self.notify_students_about_exam())
        self.get_ticket()
        print(self.get_text_start_exam())
        while self.time_now < self.time_end:
            self.time_now = datetime.datetime.now()
            self.student_answer = Student.reply()
            self.teacher_reply = self.__teacher.reply()
            self.answer = self.check_answer()
            break

        print(self.get_result_exam(self.answer))
        print(self.get_text_end_exam())

    def notify_students_about_exam(self):
        return f'Уважаемые студенты группы {self.__student_group.number} {self.__student_group.qualification}!\n' \
               f'{'\n'.join([student['name'] for student in self.__student_group])} \n\n' \
               f'Экзамен начинается! Пожалуйста, уберите электронные приборы в рюкзак и сдайте зачетную книжку преподавателю ' \
               f'{self.__teacher.name} \n'

    def get_text_start_exam(self):
        return self.time_now.strftime(self.FORMATTED_TIME)

    def get_text_end_exam(self):
        return self.time_end.strftime(self.FORMATTED_TIME)

    def get_ticket(self):
        for ticket in self.__ticket_generator:
            print(f'Предмет: {self.__subject} \n',
                  f'Преподаватель: {self.__teacher.name} \n',
                  f'Группа: {self.__student_group.number} \n',
                  f'Вопрос: {ticket.question} \n')

    def check_answer(self):
        return self.__statuses.PASSED if self.teacher_reply.lower() in self._answers or self.teacher_reply.lower() == self._answers \
            else self.__statuses.FAILED

    def get_result_exam(self, status):
        return self.EXAM_SUCCESS if status == 'passed' else self.EXAM_FAILED

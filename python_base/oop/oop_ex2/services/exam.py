import datetime

from ..services.ticket_generator import TicketGenerator
from python_base.oop.oop_ex2.enums.exam_statuses import ExamStatuses
from python_base.oop.oop_ex2.enums.answers import Answers


class Exam:
    FORMATTED_TIME = '%H:%M:%S'
    TEACHER_REPLY = 'yes'
    MIN_SCORE_FOR_PAY = 4.0

    def __init__(self, student_group, teacher, subject, difficulty):
        self._student_group = student_group
        self._teacher = teacher
        self._subject = subject
        self._ticket_generator = TicketGenerator(difficulty=difficulty, quantity=2).get_ticket()
        self.time_start = None
        self.time_end = None
        self.notify_students_about_exam()
        self.answer = ''

    def start(self, seconds):
        self.time_start = datetime.datetime.now()
        self.time_end = datetime.timedelta(seconds=seconds) + self.time_start
        print(self.notify_students_about_exam())
        self.get_ticket()
        print(self.get_text_start_exam())
        while self.time_start < self.time_end:
            self.time_start = datetime.datetime.now()
            self.answer = self.check_answer()
            break

        print(self.answer)
        print(self.get_text_end_exam())

    def notify_students_about_exam(self):
        return f'Уважаемые студенты группы {self._student_group.number} {self._student_group.qualification}!\n' \
               f'{'\n'.join([f"{student.name}" for student in self._student_group])} \n\n' \
               f'Экзамен начинается! Пожалуйста, уберите электронные приборы в рюкзак и сдайте зачетную книжку преподавателю ' \
               f'{self._teacher.name} \n'

    def get_text_start_exam(self):
        return self.time_start.strftime(self.FORMATTED_TIME)

    def get_text_end_exam(self):
        return self.time_end.strftime(self.FORMATTED_TIME)

    def get_ticket(self):
        for ticket in self._ticket_generator:
            print(f'Предмет: {self._subject} \n',
                  f'Преподаватель: {self._teacher.name} \n',
                  f'Группа: {self._student_group.number} \n',
                  f'Вопрос: {ticket.question} \n')

    def check_answer(self):
        return ExamStatuses.PASSED if self.TEACHER_REPLY in Answers else ExamStatuses.FAILED

    def kick_student(self, student):
        print(f'Студент {student.name} отчислен')
        self._student_group.remove_student(student)

    def pay_student(self, student):
        return f'{student.name} получает стипендию' \
            if student.avg_score >= self.MIN_SCORE_FOR_PAY else self.kick_student(student)

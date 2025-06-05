import json
import random

import faker
from faker import Faker
from ticket import Ticket


class TicketGenerator:
    DIFFICULTIES = ['easy', 'medium', 'hard']
    TIME_FOR_TICKET = [5, 15, 30]
    PATH_QUESTIONS = "questions.json"

    def __init__(self, difficulty: str, quantity, subject):
        self.difficulty = difficulty
        self.subject = subject
        self.quantity = quantity
        self.faker = Faker()
        self.questions = {}
        self.read_file()

    def __iter__(self):
        for ticket in range(self.quantity):
            question = self.get_question_by_difficulty()
            yield Ticket(question=question)

    def get_question_by_difficulty(self):
        if self.difficulty in self.DIFFICULTIES:
            for d, themes in self.questions.items():
                if d == self.difficulty:
                    for theme, questions in themes.items():
                        return random.choices(questions)
        else:
            return 'Ошибка! Необходимо ввести один из трех уровней сложностей: easy, medium, hard'

    def read_file(self):
        with open(self.PATH_QUESTIONS, 'r', encoding='utf-8') as file:
            self.questions = json.load(file)

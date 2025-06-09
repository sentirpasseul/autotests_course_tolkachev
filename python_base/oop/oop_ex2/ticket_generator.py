import json
import random
from enum import Enum, StrEnum
import faker
from faker import Faker
from ticket import Ticket


class TicketGenerator:
    DIFFICULTIES = StrEnum('DIFFICULTIES', {'EASY': 'easy', "MEDIUM": 'medium', "HARD": 'hard'})
    TIME_FOR_TICKET = Enum('TIME_FOR_TICKET', {'SHORT': 5, 'MEDIUM': 15, 'HARD': 30})
    PATH_QUESTIONS = "questions.json"

    def __init__(self, difficulty: str, quantity):
        self._difficulty = difficulty
        self._quantity = quantity
        self.__questions = {}
        self.read_file()

    def get_ticket(self):
        for ticket in range(self._quantity):
            question = self.get_question_by_difficulty()
            yield Ticket(question=question)

    def get_question_by_difficulty(self):
        if self._difficulty in self.DIFFICULTIES:
            question = self.__questions.get(f'{self._difficulty}')
            return random.choice(question.get(random.choice([theme for theme in question])))
        else:
            raise TypeError(
                f'Ошибка! Необходимо ввести один из трех уровней сложностей: '
                f'{self.DIFFICULTIES.EASY}, {self.DIFFICULTIES.MEDIUM}, {self.DIFFICULTIES.HARD}')

    def read_file(self):
        with open(self.PATH_QUESTIONS, 'r', encoding='utf-8') as file:
            self.__questions = json.load(file)

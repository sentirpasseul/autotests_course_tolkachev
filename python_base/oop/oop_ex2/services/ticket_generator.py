import json
import random
from python_base.oop.oop_ex2.models.ticket import Ticket
from python_base.oop.oop_ex2.enums.difficulties import Difficulties
from ..utils.config.settings import QUESTIONS_PATH


class TicketGenerator:
    PATH_QUESTIONS = "../utils/questions.json"

    def __init__(self, difficulty: Difficulties, quantity):
        self._difficulty = difficulty
        self._quantity = quantity
        self._questions = {}
        self.read_file()

    def get_ticket(self):
        for ticket in range(self._quantity):
            question = self.get_question()
            yield Ticket(question=question)

    def get_question(self):
        if self._difficulty not in Difficulties:
                raise TypeError(
                    f'Ошибка! Необходимо ввести один из трех уровней сложностей: ' +  ', '.join(d for d in Difficulties))

        question = self._questions.get(f'{self._difficulty}')
        return random.choice(question.get(random.choice([theme for theme in question])))

    def read_file(self):
        with open(QUESTIONS_PATH, 'r', encoding='utf-8') as file:
            self._questions = json.load(file)

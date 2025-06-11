import json
import random
from ticket import Ticket
from difficulties import Difficulties


class TicketGenerator:
    PATH_QUESTIONS = "questions.json"

    def __init__(self, difficulty: Difficulties, quantity):
        self._difficulty = difficulty
        self._quantity = quantity
        self._questions = {}
        self.read_file()

    def get_ticket(self):
        for ticket in range(self._quantity):
            question = self.get_question_by_difficulty()
            yield Ticket(question=question)

    def get_question_by_difficulty(self):
        if self._difficulty not in Difficulties:
            raise TypeError(
                f'Необходимо ввести один из трех уровней сложностей: '
                f'{Difficulties.EASY}, {Difficulties.MEDIUM}, {Difficulties.HARD}')

        questions_by_theme = self._questions.get(self._difficulty)
        theme = random.choice(list(questions_by_theme.keys()))
        return random.choice(questions_by_theme[theme])

    def get_question_by_difficulty1(self):
        if self._difficulty in Difficulties:
            question = self._questions.get(f'{self._difficulty}')
            return random.choice(question.get(random.choice([theme for theme in question])))
        else:
            raise TypeError(
                f'Ошибка! Необходимо ввести один из трех уровней сложностей: '
                f'{Difficulties.EASY}, {Difficulties.MEDIUM}, {Difficulties.HARD}')

    def read_file(self):
        with open(self.PATH_QUESTIONS, 'r', encoding='utf-8') as file:
            self._questions = json.load(file)

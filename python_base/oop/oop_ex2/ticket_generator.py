import json
import random

import faker
from faker import Faker
from ticket import Ticket


class TicketGenerator:
    def __init__(self):
        self.difficulty = ['easy', 'medium', 'hard']
        self.time = [5, 15, 30]
        self.faker = Faker()
        self.ticket = Ticket(question=self.faker.job())
        self.questions = {}
        self.read_file()

    def generate_ticket(self):
        yield self.ticket

    def get_question_by_difficulty(self, difficulty: str):
        if difficulty in self.difficulty:
            for key in self.questions:
                return self.questions.get(key)

    def read_file(self):
        with open("questions.json", 'r', encoding='utf-8') as file:
            self.questions = json.load(file)



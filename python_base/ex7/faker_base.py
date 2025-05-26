from faker import Faker


class FakerBase(Faker):
    MIN_HOURS = 10
    MAX_HOURS = 80

    def __init__(self):
        super().__init__('ru-RU')

    def get_person_name(self):
        return self.first_name() + ' ' + self.last_name()

    def get_random_int(self):
        return Faker().random_int(min=self.MIN_HOURS, max=self.MAX_HOURS)

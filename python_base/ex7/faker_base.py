from faker import Faker


class FakerBase(Faker):
    def __init__(self):
        super().__init__('ru-RU')

    def get_person_name(self):
        return self.first_name() + ' ' + self.last_name()

    def get_subject(self):
        return self.random_int(min=10, max=80)

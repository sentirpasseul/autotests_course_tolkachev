from faker import Faker


class FakerBase(Faker):
    RANDOM_INT = Faker().random_int(min=10, max=80)

    def __init__(self):
        super().__init__('ru-RU')
        self.subject = self.RANDOM_INT

    def get_person_name(self):
        return self.first_name() + ' ' + self.last_name()

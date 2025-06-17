from person import Person


class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)

    def study(self):
        return f'{self.name} учится'

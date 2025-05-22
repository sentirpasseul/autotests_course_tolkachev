class Subject:
    def __init__(self, name, hours):
        self.name = ''
        self.hours = ''

    def __str__(self):
        return f'{self.name}, {self.hours}'

    @staticmethod
    def get_name(name):
        return name

    @staticmethod
    def get_hours(hours):
        return hours

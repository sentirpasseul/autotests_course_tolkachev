class Subject:
    def __init__(self, name_subject: str, hours_subject: int):
        self.name = name_subject
        self.hours = hours_subject

    def __str__(self):
        return f'предмет {self.name}'

    def get_hours(self):
        return self.hours

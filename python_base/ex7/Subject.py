class Subject:
    def __init__(self, name_subject: str, hours_subject: int):
        self.name = name_subject
        self.hours = hours_subject

    def get_subject_name(self):
        return f'{self.name}'

    def get_subject_hours(self):
        return self.hours
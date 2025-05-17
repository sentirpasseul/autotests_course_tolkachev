class Subject:
    def __init__(self, name_subject: str, hours_subject: int):
        self.name_subject = name_subject
        self.hours_subject = hours_subject

    def get_subject_name(self):
        return f'{self.name_subject}'

    def get_subject_hours(self):
        return self.hours_subject
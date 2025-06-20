class Schedule:
    def __init__(self):
        self.schedule = {}

    def add_lessons_at_schedule(self, teachers, groups, subjects):
        for teacher, group, subject in zip(teachers, groups, subjects):
            self.schedule[teacher] = {
                "subject": subject,
                "group": [student for student in group]
            }

    def __len__(self):
        return len(self.schedule)

    def __eq__(self, other):
        return len(self) == len(other)

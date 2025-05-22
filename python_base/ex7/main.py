import random

from subject import Subject
from student import Student
from teacher import Teacher
from schedule import Schedule
from faker_base import FakerBase
from assistant import Assistant


class MainApp:
    def __init__(self):
        self.faker = FakerBase()
        self.subject = Subject(self.faker.job(), self.faker.random_int(min=10, max=80))
        self.subjects = {self.faker.job(): Subject(self.faker.job(), self.faker.random_int(min=10, max=80))
                         for _ in range(10)}

        self.group_math1 = [Student(self.faker.get_person_name()).name for _ in range(10)]
        self.group_chemistry1 = [Student(self.faker.get_person_name()).name for _ in range(20)]
        self.groups = [self.group_math1, self.group_chemistry1]

        self.teachers = {Teacher(self.faker.get_person_name()).name: Teacher.SPARE_TIME for _ in range(10)}

        self.schedule = Schedule()
        self.schedule.add_lessons_at_schedule(teachers=self.teachers, groups=self.groups,
                                              subjects=self.subjects)

        self.assistant = Assistant(teacher_name=random.choice(list(self.teachers.keys())),
                                   student_name=self.groups[random.randint(0, 1)][random.randint(0, 9)],
                                   grade=str(random.randint(1, 5)))

    def get_objects(self):
        return f'Преподаватели: {self.teachers}' \
               f'\nГруппа математики: {self.group_math1}' \
               f'\nГруппа химии: {self.group_chemistry1}' \
               f'\nРасписание: {self.schedule.schedule}' \
               f'\nПредметы: {[subject for subject in self.subjects]}' \
               f'\nАссистент: {self.assistant}' \
               f'\nАсссистент {self.assistant.teach()}{self.groups[random.randint(0, 1)][random.randint(0, 9)]}'

    def print_instance_schedule(self):
        if not self.schedule:
            return 'Расписание пока не заполнено. Его следует заполнить'
        else:
            return ''


def main():
    app = MainApp()
    print(app.get_objects())
    print(app.print_instance_schedule())


if __name__ == '__main__':
    main()

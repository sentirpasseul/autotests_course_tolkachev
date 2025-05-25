import random

from subject import Subject
from student import Student
from teacher import Teacher
from schedule import Schedule
from faker_base import FakerBase


class MainApp:
    def __init__(self):
        self.faker = FakerBase()
        self.subjects = {self.faker.job(): Subject(self.faker.job())
                         for _ in range(10)}

        self.group_math1 = [Student(self.faker.get_person_name()) for _ in range(10)]
        self.group_chemistry1 = [Student(self.faker.get_person_name()) for _ in range(20)]
        self.groups = [self.group_math1, self.group_chemistry1]

        self.teachers = {Teacher(self.faker.get_person_name()): Teacher.SPARE_TIME for _ in range(10)}

        self.schedule = Schedule()
        self.schedule.add_lessons_at_schedule(teachers=self.teachers, groups=self.groups,
                                              subjects=self.subjects)

    def get_objects(self):
        return f'Преподаватели: {self.teachers}' \
               f'\nГруппа математики: {self.group_math1}' \
               f'\nГруппа химии: {self.group_chemistry1}' \
               f'\nРасписание: {self.schedule.schedule}' \
               f'\nПредметы: {[subject for subject in self.subjects]}'

    def execute(self):
        self.get_lessons() if self.schedule.schedule else 'Расписание пока не заполнено. Его следует заполнить'

    def get_lessons(self):
        result = []
        for teacher, group, subject in zip(list(self.teachers), self.groups, list(self.subjects)):
            print('Группа: ', [student.name for student in group])
            print(teacher.teach_student())
            print('Предмет:', subject)
            for student in group:
                print('Студент', student.study())
            print('\n\n')


def main():
    app = MainApp()
    app.execute()


if __name__ == '__main__':
    main()

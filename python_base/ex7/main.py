from subject import Subject
from student import Student
from teacher import Teacher
from schedule import Schedule
from faker_base import FakerBase


class MainApp:
    def __init__(self):
        self.faker = FakerBase()
        self.math = Subject("Математика", 40)
        self.chemistry = Subject('Химия', 60)

        self.group_math1 = [Student(self.faker.get_person_name()).name for _ in range(10)]
        self.group_chemistry1 = [Student(self.faker.get_person_name()).name for _ in range(20)]

        self.teachers = {Teacher(self.faker.get_person_name()).name: 140 for _ in range(10)}

        self.schedule = Schedule()
        self.schedule.add_lessons_at_schedule(teachers=self.teachers, groups=[self.group_math1, self.group_chemistry1],
                                              subjects=[self.math, self.chemistry])

    def get_objects(self):
        return f'Преподаватели: {self.teachers}' \
               f'\nГруппа математики: {self.group_math1}' \
               f'\nГруппа химии:{self.group_chemistry1}' \
               f'\nРасписание: {self.schedule.schedule}'

    def print_instance_schedule(self):
        if self.schedule.__eq__(0):
            return 'Расписание пока не заполнено. Его следует заполнить'
        else:
            return ''


def main():
    app = MainApp()
    print(app.get_objects())
    print(app.print_instance_schedule())


if __name__ == '__main__':
    main()

# print(Student(faker.get_person_name()), 'TEST')

"""""
for teacher in range(len(teachers)):
    schedule.add_lesson_at_schedule(teacher=teacher, student=student, subject=subject)
"""""

# print(schedule.add_teacher(teacher1))
# print(schedule.schedule)
# print(teacher1.teach_student())

# print(group_chemistry1)

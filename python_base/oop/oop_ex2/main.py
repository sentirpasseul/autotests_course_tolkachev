from exam import Exam
from faker import Faker
from student_group import StudentGroup
from teacher import Teacher
from subject import Subject
from student import Student
import random

if __name__ == '__main__':
    # try:
    faker = Faker('ru_RU')
    student = Student
    subject = Subject(name=faker.job())
    teacher = Teacher(name=faker.name(), age=random.randint(student.MIN_AGE, student.MAX_AGE),
                      qualification=faker.job())
    student_group = StudentGroup(number='B618', qualification='MOAIS')
    for _ in range(10):
        student_group.add_student_in_group(Student(name=faker.name(),
                                                   age=random.randint(
                                                       student.MIN_AGE,
                                                       student.MAX_AGE),
                                                   avg_score=round(
                                                       random.uniform(
                                                           subject.MIN_SCORE,
                                                           subject.MAX_SCORE
                                                       ), 2)))
    print(student_group.students)
    exam = Exam(student_group=student_group, teacher=teacher, subject=subject, difficulty='medium')
    exam.start(2)

    # except:
    #     TypeError: print("Ошибка TypeError")

from python_base.oop.oop_ex2.services.exam import Exam
from faker import Faker
from python_base.oop.oop_ex2.models.student_group import StudentGroup
from python_base.oop.oop_ex2.models.teacher import Teacher
from python_base.oop.oop_ex2.models.subject import Subject
from python_base.oop.oop_ex2.models.student import Student
import random


def main():
    faker = Faker('ru_RU')
    subject = Subject(name=faker.job())
    teacher = Teacher(name=faker.name(), age=random.randint(Student.MIN_AGE, Student.MAX_AGE),
                      qualification=faker.job())
    student_group = StudentGroup(number='B618', qualification='MOAIS')
    for _ in range(10):
        student_group.add_student(Student(name=faker.name(),
                                          age=random.randint(Student.MIN_AGE, Student.MAX_AGE),
                                          avg_score=round(random.uniform(Subject.MIN_SCORE, Subject.MAX_SCORE),
                                                          2)
                                          )
                                  )
    exam = Exam(student_group=student_group, teacher=teacher, subject=subject, difficulty='medium')
    exam.start(2)
    print(student_group.get_student(2))
    #print(exam.pay_student(student_group.get_student(2)))


if __name__ == '__main__':
    # try:
    main()

    # except Exception as e:
    #     logging.warning(f'{e}')

class StudentGroup:
    MIN_SCORE_FOR_PAY = 4

    def __init__(self, number, qualification):

        self.__students = {}
        self.number = number
        self.qualification = qualification

    def __iter__(self):
        return iter(self.__students.values())

    def __len__(self):
        return len(self.__students)

    def __eq__(self, other):
        if isinstance(other, StudentGroup):
            return len(self) == len(other)

    def __str__(self):
        return f'{self.__students}'

    def add_student(self, student):
        self.__students[student.id] = {
            'name': student.name,
            'age': student.age,
            'avg_score': student.avg_score
        }
        return self.__students

    def kick_students(self):
        for student in self.__students.values():
            if student.get('avg_score') < self.MIN_SCORE_FOR_PAY:
                print(self.get_text_kicked_students(student))
                
    def get_text_kicked_students(self, student):
        return f'Студент {student.get('name')} отчислен'

    def pay_students(self, student):
        if student.exam_score >= self.MIN_SCORE_FOR_PAY:
            return f'{student.name} получает стипендию'

    def get_student(self, key):
        return self.__students.get(key)

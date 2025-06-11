class StudentGroup:
    MIN_SCORE_FOR_PAY = 4.0

    def __init__(self, number, qualification):
        self._students = []
        self.number = number
        self.qualification = qualification

    def __iter__(self):
        return iter(self._students)

    def __len__(self):
        return len(self._students)

    def __eq__(self, other):
        return len(self) == len(other) if isinstance(other, StudentGroup) else False

    def __str__(self):
        return f'{self._students}'

    def add_student(self, student):
        self._students.append(student)
        return self._students

    def kick_student(self, student):
        print(self.get_text_kicked_students(student))
        self._students.pop(student)

    def get_text_kicked_students(self, student):
        return f'Студент {student.name} отчислен'

    def pay_student(self, student):
        return f'{student.name} получает стипендию' \
            if student.avg_score >= self.MIN_SCORE_FOR_PAY else self.kick_student(student)

    def get_student(self, key):
        return self._students.__getitem__(key)

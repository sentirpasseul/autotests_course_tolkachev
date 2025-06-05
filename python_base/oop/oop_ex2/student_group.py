class StudentGroup:
    def __init__(self, number, qualification):
        self.students = {}
        self.number = number
        self.qualification = qualification
        self.index = 0

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.students)

    def __eq__(self, other):
        if isinstance(other, StudentGroup):
            return len(self) == len(other)

    def __next__(self):
        if self.index < len(self.students.keys()):
            key = self.students.keys[self.index]
            value = self.students[key]
            self.index += 1
            return key, value
        else:
            raise StopIteration

    def add_student_in_group(self, student):
        self.students[student.id] = {
            'name': student.name,
            'age': student.age,
            'avg_score': student.avg_score
        }
        return self.students

    def kick_student(self, student):
        if student.exam_score < 4:
            return f'{student.name} отчислен'

    def pay_students(self, student):
        if student.exam_score >= 4:
            return f'{student.name} получает стипендию'


class StudentGroup():
    def __init__(self, grade, qualification):
        self.students = {}
        self.grade = grade
        self.qualification = qualification

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.students)

    def __eq__(self, other):
        pass

    def __next__(self):
        pass

    def add_student_in_group(self, student):
        self.students[student.id] = {
            'name': student.name,
            'age': student.age,
            'avg_score': student.avg_score
        }

    def notify_students(self):
        pass

    def kick_student(self):
        pass

    def pay_students(self):
        pass

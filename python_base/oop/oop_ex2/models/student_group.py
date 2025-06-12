class StudentGroup:

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

    def get_student(self, key):
        return self._students.__getitem__(key)

    def remove_student(self, student):
        self._students.pop(student)
        return self._students

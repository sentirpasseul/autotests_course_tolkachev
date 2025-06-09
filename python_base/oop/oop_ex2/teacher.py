from human import Human


class Teacher(Human):
    _id_counter = 1

    def __init__(self, name: str, age: int, qualification: str):
        super().__init__(name=name, age=age)
        self.id = Teacher._id_counter
        Teacher._id_counter += 1
        self.qualification = qualification

    def __str__(self):
        return f'{self.name} {self.age} {self.qualification}'

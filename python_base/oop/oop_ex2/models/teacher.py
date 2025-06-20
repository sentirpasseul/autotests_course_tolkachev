from python_base.oop.oop_ex2.models.human import Human


class Teacher(Human):

    def __init__(self, name: str, age: int, qualification: str):
        super().__init__(name=name, age=age)
        self.qualification = qualification

    def __str__(self):
        return f'{self.name} {self.age} {self.qualification}'

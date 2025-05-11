class Exercise5:
    def __init__(self):
        self.__var = 'private_parent'
        self._protected = 'protected_parent'  # 5.4


class Ex5_5(Exercise5):
    def __init__(self):
        self.__var = 'private_child'
        super().__init__()


exercise_5 = Exercise5()
new_exercise_5 = Ex5_5()
print("5.2: ", vars(exercise_5))
print("5.3: ", exercise_5._Exercise5__var)
print("5.4-5.5: ", exercise_5._protected, new_exercise_5._protected)
print("5.7: ", vars(Ex5_5))
print("")

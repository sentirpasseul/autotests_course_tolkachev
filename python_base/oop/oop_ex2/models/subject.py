class Subject:
    MIN_SCORE = 2.0
    MAX_SCORE = 5.0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

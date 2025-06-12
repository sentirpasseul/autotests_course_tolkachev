from enum import StrEnum


class ExamStatuses(StrEnum):
    PASSED = 'Экзамен сдан. Поздравляем!'
    FAILED = 'Экзамен провален.'

import random
from enum import StrEnum


class ExamStatus(StrEnum):
    PASSED = 'passed'
    CANCELED = 'canceled'
    IN_PROGRESS = 'in progress'
    FAILED = 'failed'

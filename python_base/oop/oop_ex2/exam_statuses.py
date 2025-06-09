from enum import StrEnum


class ExamStatuses(StrEnum):
    PASSED = 'passed'
    CANCELED = 'canceled'
    IN_PROGRESS = 'in progress'
    FAILED = 'failed'

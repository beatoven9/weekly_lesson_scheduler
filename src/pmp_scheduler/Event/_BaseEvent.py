from typing import List, Optional

from pmp_scheduler.Person import Student, Teacher
from pmp_scheduler.Time import TimeBlock


class BaseEvent:
    def __init__(
        self,
        label: Optional[str],
        time_blocks: List[TimeBlock],
    ):
        self.label = label
        self.time_blocks = time_blocks


class BaseStudentEvent(BaseEvent):
    def __init__(
        self,
        label: Optional[str],
        time_blocks: List[TimeBlock],
        students: List[Student],
        teachers: Optional[Teacher],
    ):
        super().__init__(label, time_blocks)
        self.students = students
        self.teachers = teachers


class GenericEvent(BaseStudentEvent):
    def __init__(
        self,
        label: Optional[str],
        time_blocks: List[TimeBlock],
        students: List[Student],
        teachers: Optional[Teacher],
    ):
        super().__init__(label, time_blocks, students, teachers)

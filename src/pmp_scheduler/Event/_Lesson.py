from typing import List, Optional

from pmp_scheduler.Person import Student, Teacher
from pmp_scheduler.Time import TimeBlock

from ._BaseEvent import BaseStudentEvent


class Lesson(BaseStudentEvent):
    def __init__(
        self,
        label: Optional[str],
        time_blocks: List[TimeBlock],
        students: List[Student],
        teachers: Optional[Teacher],
    ):
        super().__init__(label, time_blocks, students, teachers)

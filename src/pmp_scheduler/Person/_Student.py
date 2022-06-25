from typing import List

from pmp_scheduler.Event import GenericEvent, GroupClass, Lesson
from pmp_scheduler.Time import TimeBlock

from ._Base_Person import Person
from ._Person_Types import EventDict, Instrument


class Student(Person):
    def __init__(
        self,
        name: str,
        instrument: Instrument,
        free_blocks: EventDict,
        group_classes: EventDict,
        lessons: EventDict,
        generic_events: EventDict,
        lessons_to_schedule: List[str],
        chamber_group_id: int,
    ):
        super().__init__(
            name,
            instrument,
            free_blocks,
            group_classes,
            lessons,
            generic_events,
        )
        self.lessons_to_schedule = lessons_to_schedule
        self.chamber_group_id = chamber_group_id

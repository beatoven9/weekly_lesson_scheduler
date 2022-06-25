from pmp_scheduler.Event import GroupClass, Lesson
from pmp_scheduler.Time import TimeBlock

from ._Person_Types import EventDict, Instrument


class Person:
    def __init__(
        self,
        name: str,
        instrument: Instrument,
        free_blocks: EventDict,
        group_classes: EventDict,
        lessons: EventDict,
        generic_events: EventDict,
    ):
        self.name = name
        self.instrument = instrument
        self.free_blocks = free_blocks
        self.group_classes = group_classes
        self.lessons = lessons
        self.generic_events = generic_events

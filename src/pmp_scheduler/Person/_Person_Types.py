from typing import List, Literal, TypedDict, Union

from pmp_scheduler.Event import FreeBlock, GenericEvent, GroupClass, Lesson

Instrument = Literal["violin", "viola", "cello"]

EventTypes = Union[Lesson, GroupClass, GenericEvent, FreeBlock]


class EventDict(TypedDict):
    Sunday: List[EventTypes]
    Monday: List[EventTypes]
    Tuesday: List[EventTypes]
    Wednesday: List[EventTypes]
    Thursday: List[EventTypes]
    Friday: List[EventTypes]
    Saturday: List[EventTypes]

from typing import List, Optional

from pmp_scheduler.Time import TimeBlock

from ._BaseEvent import BaseEvent


class FreeBlock(BaseEvent):
    def __init__(
        self,
        label: Optional[str],
        time_blocks: List[TimeBlock],
    ):
        super().__init__(label, time_blocks)

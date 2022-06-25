from datetime import datetime


class TimeBlock:
    def __init__(
        self,
        start_time: datetime,
        end_time: datetime,
    ):
        self.start_time = start_time
        self.end_time = end_time

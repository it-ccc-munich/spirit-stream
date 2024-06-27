from datetime import date
from typing import List


class SundayServiceReportDTO:
    def __init__(self, sunday_service_date: date, greeters: List[str], adults_attended: int, children_attended: int, newcomer: int, offering: float):
        # 接待
        self.greeters = greeters
        self.sunday_service_date = sunday_service_date
        self.adults_attended = adults_attended
        self.children_attended = children_attended
        self.newcomer = newcomer
        self.offering = offering

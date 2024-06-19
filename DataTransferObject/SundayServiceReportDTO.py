from datetime import date


class SundayServiceReportDTO:
    def __init__(self, sunday_service_date: date, adults_attended: int, children_attended: int, newcomer: int, offering: float):

        self.sunday_service_date = sunday_service_date
        self.adults_attended = adults_attended
        self.children_attended = children_attended
        self.newcomer = newcomer
        self.offering = offering

import datetime

import gspread

from DataTransferObject.SundayServiceReportDTO import SundayServiceReportDTO
from GoogleSheets.DateHelper import find_date_index


def _dict2dto(date, result_dict) -> SundayServiceReportDTO:

    try:
        adults_attended = int(result_dict['成人'])
    except ValueError:
        adults_attended = None

    try:
        children_attended = int(result_dict['小孩'])
    except ValueError:
        children_attended = None

    try:
        newcomer = int(result_dict['新人'])
    except ValueError:
        newcomer = None

    try:
        offering = float(result_dict['奉獻'].replace('€', ''))
    except ValueError:
        offering = None

    return SundayServiceReportDTO(
        sunday_service_date=date,
        adults_attended=adults_attended,
        children_attended=children_attended,
        newcomer=newcomer,
        offering=offering
    )


class SundayServiceStatisticsConnector:

    def __init__(self, service_account_json_path):

        gc = gspread.service_account(service_account_json_path)
        self.spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1N3qkcK6iVPtIKX_TEJboDadS0TrjUgUw0lzM4lFIUnc/edit?usp=sharing')
        self.worksheet = self.spreadsheet.worksheet('2024')

    def get_service_statistics(self, target_date: datetime.date) -> SundayServiceReportDTO:
        row_index = find_date_index(target_date, self.worksheet)

        dict_for_row = {}

        keys = self.worksheet.get(f"A1:E1")[0]
        values = self.worksheet.get(f"A{row_index}:E{row_index}")[0]

        assert len(keys) == len(values)

        for i in range(len(keys)):
            dict_for_row[keys[i]] = values[i]

        return _dict2dto(target_date, dict_for_row)

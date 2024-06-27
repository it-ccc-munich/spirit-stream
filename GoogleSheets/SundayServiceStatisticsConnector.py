import datetime

import gspread

from DataTransferObject.SundayServiceReportDTO import SundayServiceReportDTO
from GoogleSheets.DateHelper import find_date_index


def _dict2dto(date, result_dict) -> SundayServiceReportDTO:

    try:
        adults_attended = int(result_dict['成人'])
    except (ValueError, KeyError):
        adults_attended = None

    try:
        children_attended = int(result_dict['小孩'])
    except (ValueError, KeyError):
        children_attended = None

    try:
        newcomer = int(result_dict['新人'])
    except (ValueError, KeyError):
        newcomer = None

    try:
        offering = float(result_dict['奉獻'].replace('€', ''))
    except (ValueError, KeyError):
        offering = None

    greeters = [result_dict['接待1'], result_dict['接待2']]

    return SundayServiceReportDTO(
        greeters=greeters,
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

        keys = self.worksheet.get(f"A1:G1")[0]
        values = self.worksheet.get(f"A{row_index}:G{row_index}")[0]

        for i in range(min(len(keys), len(values))):
            dict_for_row[keys[i]] = values[i]

        return _dict2dto(target_date, dict_for_row)

import datetime

import gspread
from gspread import Worksheet

from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from GoogleSheets.DateHelper import find_date_index


def _dict2dto(target_date, result_dict):
    # jiawen, for weekly report

    return SundayServiceStaffDTO(
        sunday_service_date=target_date,
        preacher=result_dict['讲员'],
        host=result_dict['主礼'],
        scripture_reader=result_dict['主礼'],
        pianist=result_dict['司琴'],
        hymn_leaders=[result_dict['主领'], result_dict['副领']],
        projector_operator=result_dict['PPT制作'],
        benediction='',
        sunday_school_leaders=[result_dict['儿主大班'], result_dict['儿主小班']],
        venue=[result_dict['场地1'], result_dict['场地2']],
        greeters=[],
        meal_preparers=[result_dict['饭食采购'], result_dict['主厨'], result_dict['帮厨1'], result_dict['帮厨2']],
        fellowship=result_dict['餐后打扫']
    )


def _read_sunday_service_staff(row_index, worksheet: Worksheet):
    # extract information from 同工表 and save in a dictionary
    # e.g., {"场地": Name}
    # author ：jiawen
    dict_for_row = {}

    keys = worksheet.get(f"A2:R2")[0]
    values = worksheet.get(f"A{row_index}:R{row_index}")[0]

    assert len(keys) == len(values)

    for i in range(len(keys)):
        dict_for_row[keys[i]] = values[i]

    return dict_for_row


class SundayServiceStaffConnector:

    def __init__(self, service_account_json_path):

        gc = gspread.service_account(service_account_json_path)
        self.spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1mF3DKEHQXaNPNYvc4_oqOtTL7xCw-TpwQaCTNYO5NA0/edit?usp=sharing')
        self.staff_worksheet = self.spreadsheet.worksheet('2024排班')

    def get_sunday_service_staff_data(self, target_date: datetime.date) -> SundayServiceStaffDTO:
        row_index = find_date_index(target_date, self.staff_worksheet)
        dict_for_row_index = _read_sunday_service_staff(row_index=row_index, worksheet=self.staff_worksheet)
        return _dict2dto(target_date, dict_for_row_index)

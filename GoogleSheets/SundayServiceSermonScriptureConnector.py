import datetime

import gspread
from DataTransferObject.SundayServiceSermonAndScripturesDTO import SundayServiceSermonAndScripturesDTO
from DataTransferObject.VerseDTO import VerseDTO
from GoogleSheets.DateHelper import find_date_index


def _dict2dto(date, result_dict) -> SundayServiceSermonAndScripturesDTO:

    try:
        psalms_of_inspiration_start = VerseDTO(result_dict['启应诗 - 書'], int(result_dict['启应诗 - 章']), int(result_dict['启应诗 - 節'].split('-')[0]))
    except ValueError:
        psalms_of_inspiration_start = None

    try:
        psalms_of_inspiration_end = VerseDTO(result_dict['启应诗 - 書'], int(result_dict['启应诗 - 章']), int(result_dict['启应诗 - 節'].split('-')[1]))
    except ValueError:
        psalms_of_inspiration_end = None

    try:
        scripture_start = VerseDTO(result_dict['經文 - 書'], int(result_dict['經文 - 章']), int(result_dict['經文 - 節'].split('-')[0]))
    except ValueError:
        scripture_start = None

    try:
        scripture_end = VerseDTO(result_dict['經文 - 書'], int(result_dict['經文 - 章']), int(result_dict['經文 - 節'].split('-')[1]))
    except ValueError:
        scripture_end = None

    try:
        golden_verse = VerseDTO(result_dict['金句 - 書'], int(result_dict['金句 - 章']), int(result_dict['金句 - 節']))
    except ValueError:
        golden_verse = None

    return SundayServiceSermonAndScripturesDTO(
        sunday_service_date=date,
        preacher=result_dict['讲员'],
        psalms_of_inspiration_start=psalms_of_inspiration_start,
        psalms_of_inspiration_end=psalms_of_inspiration_end,
        scripture_start=scripture_start,
        scripture_end=scripture_end,
        teaching_title=result_dict['主題'],
        benediction=result_dict['祝福'],
        golden_verse=golden_verse
    )


class SundayServiceSermonScriptureConnector:

    def __init__(self, service_account_json_path):

        gc = gspread.service_account(service_account_json_path)
        self.spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1sc81EAGM9jl6aj3rM39etH7IDsj4x14N6f0P7Y952rA/edit?usp=sharing')
        self.worksheet = self.spreadsheet.worksheet('2024')

    def get_sermon_scripture_data(self, target_date: datetime.date) -> SundayServiceSermonAndScripturesDTO:
        row_index = find_date_index(target_date, self.worksheet)

        dict_for_row = {}

        keys = self.worksheet.get(f"A2:R2")[0]
        values = self.worksheet.get(f"A{row_index}:R{row_index}")[0]

        assert len(keys) == len(values)

        for i in range(len(keys)):
            dict_for_row[keys[i]] = values[i]

        return _dict2dto(target_date, dict_for_row)

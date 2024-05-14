import datetime

import gspread

from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from GoogleSheets.StaffWorksheetHelper import find_date_index, read_sunday_service_staff, dict2dto


class SundayServiceStaffAndContactGoogleSheets:

    def __init__(self, service_account_json_path, share_link):

        gc = gspread.service_account(service_account_json_path)
        self.spreadsheet = gc.open_by_url(share_link)
        self.staff_worksheet = self.spreadsheet.worksheet('2024排班')
        self.contact_worksheet = self.spreadsheet.worksheet('邮件列表')

    def get_sunday_service_staff_data(self, target_date: datetime.date) -> SundayServiceStaffDTO:
        row_index = find_date_index(target_date, self.staff_worksheet)
        dict_for_row_index = read_sunday_service_staff(row_index=row_index, worksheet=self.staff_worksheet)
        return dict2dto(target_date, dict_for_row_index)

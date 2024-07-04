from typing import List
import gspread
from DataTransferObject.ContactDTO import ContactDTO


class ServiceStaffContactInfoConnector:

    def __init__(self, service_account_json_path):

        gc = gspread.service_account(service_account_json_path)
        self.spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/18Ogb_M0DV5YOtzKsMTKyoKQlZcMZJZJ2M9lADaICFBo/edit?usp=sharing')
        self.contact_info_worksheet = self.spreadsheet.worksheet('邮件列表')

    def get_contact_info_data(self) -> List[ContactDTO]:
        return self.read_contact_info()

    def read_contact_info(self) -> List[ContactDTO]:
        result = []

        for i in range(2, self.contact_info_worksheet.row_count + 1):
            row_values = self.contact_info_worksheet.row_values(i)
            if len(row_values) == 0:
                break
            result.append(ContactDTO(row_values[0], row_values[1], row_values[2:]))

        return result

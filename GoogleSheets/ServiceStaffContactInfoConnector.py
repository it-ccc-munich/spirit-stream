from typing import List
import gspread
from DataTransferObject.ContactDTO import ContactDTO


class ServiceStaffContactInfoConnector:

    def __init__(self, service_account_json_path):

        gc = gspread.service_account(service_account_json_path)
        self.spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1mF3DKEHQXaNPNYvc4_oqOtTL7xCw-TpwQaCTNYO5NA0/edit?usp=sharing')
        self.contact_info_worksheet = self.spreadsheet.worksheet('邮件列表')

    def get_contact_info_data(self) -> List[ContactDTO]:
        return self.read_contact_info()

    def read_contact_info(self) -> List[ContactDTO]:
        result = []

        names = self.contact_info_worksheet.col_values(1)
        emails = self.contact_info_worksheet.col_values(2)

        assert len(names) == len(emails)

        for i in range(1, len(names)):  # We skip row 0 because it is the header.
            result.append(ContactDTO(names[i], emails[i]))

        return result

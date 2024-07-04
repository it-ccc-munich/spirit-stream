import copy
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

from DataTransferObject.ContactDTO import ContactDTO
from DataTransferObject.SundayServiceSermonAndScripturesDTO import SundayServiceSermonAndScripturesDTO
from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from HtmlTemplates.TemplateStringReplacement import replace_this_week_service_staff
from Security.GoogleAccountAppPassword import GoogleAccountAppPassword


class EmailService:

    def __init__(self):

        self.email_address = "it.ccc.munich@gmail.com"
        self.password = GoogleAccountAppPassword.secret.replace(' ', '')

    def send_email(self, message: MIMEMultipart):
        message['From'] = self.email_address

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_address, self.password)
            smtp.sendmail(self.email_address, message["To"], message.as_string())

    def send_service_reminder_emails(self, sunday_service_staff: SundayServiceStaffDTO, sunday_service_sermon_and_scriptures: SundayServiceSermonAndScripturesDTO, weekly_report_url: str, contacts: List[ContactDTO]):
        filedir = os.path.dirname(__file__)
        file = open(os.path.join(filedir, "./ServiceReminderEmailTemplate.html"), "r", encoding="utf-8")
        content = file.read()
        file.close()

        for contact in contacts:
            # 如果聯係清單上的名字出現在本周服侍裏 并且 聯係人有email記錄在聯係清單上
            if contact.email:
                contact_name_list = [i for i in contact.alias]
                contact_name_list.append(contact.name)

                sunday_service_staff_c = copy.deepcopy(sunday_service_staff)
                sunday_service_sermon_and_scriptures_c = copy.deepcopy(sunday_service_sermon_and_scriptures)
                # 加粗名字
                name_in_service_staff = self._replace_matching_names_in_service_staff_with_bold(sunday_service_staff_c, contact_name_list)
                name_in_sermon_and_scriptures = self._replace_matching_names_in_sermon_and_scriptures_with_bold(sunday_service_sermon_and_scriptures_c, contact_name_list)
                if not name_in_service_staff and not name_in_sermon_and_scriptures:
                    continue
                content_to_send = replace_this_week_service_staff(content, sunday_service_staff_c,
                                                                  sunday_service_sermon_and_scriptures_c)
                content_to_send = content_to_send.replace('%THIS_WEEKLY_REPORT_URL%', weekly_report_url)

                # 發送郵件
                message = MIMEMultipart('alternative')

                message["To"] = contact.email
                message["Subject"] = f'{sunday_service_staff_c.sunday_service_date.strftime("%Y-%m-%d")} 服侍提醒'

                message.attach(MIMEText(content_to_send, 'html'))

                self.send_email(message)

    @staticmethod
    def _replace_matching_names_in_service_staff_with_bold(sunday_service_staff: SundayServiceStaffDTO, contact_name_list: List[str]) -> bool:
        name_contained = False
        if sunday_service_staff.host in contact_name_list:
            sunday_service_staff.host = f'<strong>{sunday_service_staff.host}</strong>'
            name_contained = True

        if sunday_service_staff.scripture_reader in contact_name_list:
            sunday_service_staff.scripture_reader = f'<strong>{sunday_service_staff.scripture_reader}</strong>'
            name_contained = True

        if sunday_service_staff.pianist in contact_name_list:
            sunday_service_staff.pianist = f'<strong>{sunday_service_staff.pianist}</strong>'
            name_contained = True

        if sunday_service_staff.projector_operator in contact_name_list:
            sunday_service_staff.projector_operator = f'<strong>{sunday_service_staff.projector_operator}</strong>'
            name_contained = True

        if sunday_service_staff.fellowship in contact_name_list:
            sunday_service_staff.fellowship = f'<strong>{sunday_service_staff.fellowship}</strong>'
            name_contained = True

        for i in range(0, len(sunday_service_staff.hymn_leaders)):
            if sunday_service_staff.hymn_leaders[i] in contact_name_list:
                sunday_service_staff.hymn_leaders[i] = f'<strong>{sunday_service_staff.hymn_leaders[i]}</strong>'
                name_contained = True

        for i in range(0, len(sunday_service_staff.sunday_school_leaders)):
            if sunday_service_staff.sunday_school_leaders[i] in contact_name_list:
                sunday_service_staff.sunday_school_leaders[i] = f'<strong>{sunday_service_staff.sunday_school_leaders[i]}</strong>'
                name_contained = True

        for i in range(0, len(sunday_service_staff.venue)):
            if sunday_service_staff.venue[i] in contact_name_list:
                sunday_service_staff.venue[i] = f'<strong>{sunday_service_staff.venue[i]}</strong>'
                name_contained = True

        for i in range(0, len(sunday_service_staff.greeters)):
            if sunday_service_staff.greeters[i] in contact_name_list:
                sunday_service_staff.greeters[i] = f'<strong>{sunday_service_staff.greeters[i]}</strong>'
                name_contained = True

        for i in range(0, len(sunday_service_staff.meal_preparers)):
            if sunday_service_staff.meal_preparers[i] in contact_name_list:
                sunday_service_staff.meal_preparers[i] = f'<strong>{sunday_service_staff.meal_preparers[i]}</strong>'
                name_contained = True

        return name_contained

    @staticmethod
    def _replace_matching_names_in_sermon_and_scriptures_with_bold(sunday_service_sermon_and_scriptures: SundayServiceSermonAndScripturesDTO, contact_name_list: List[str]) -> bool:
        name_contained = False
        if sunday_service_sermon_and_scriptures.preacher in contact_name_list:
            sunday_service_sermon_and_scriptures.preacher = f'<strong>{sunday_service_sermon_and_scriptures.preacher}</strong>'
            name_contained = True

        if sunday_service_sermon_and_scriptures.benediction in contact_name_list:
            sunday_service_sermon_and_scriptures.benediction = f'<strong>{sunday_service_sermon_and_scriptures.benediction}</strong>'
            name_contained = True

        return name_contained

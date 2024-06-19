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

    def send_service_reminder_emails(self, sunday_service_staff: SundayServiceStaffDTO, sunday_service_sermon_and_scriptures: SundayServiceSermonAndScripturesDTO, contacts: List[ContactDTO]):
        file = open("./ServiceReminderEmailTemplate.html", "r", encoding="utf-8")
        content = file.read()
        file.close()

        content = replace_this_week_service_staff(content, sunday_service_staff, sunday_service_sermon_and_scriptures)

        for contact in contacts:
            # 如果聯係清單上的名字出現在本周服侍裏 并且 聯係人有email記錄在聯係清單上
            if contact.name in content and contact.email:
                # 加粗名字
                content = content.replace(contact.name, f'<strong>{contact.name}</strong>')
                # 發送郵件
                message = MIMEMultipart('alternative')

                message["To"] = contact.email
                message["Subject"] = f'{sunday_service_staff.sunday_service_date.strftime("%Y-%m-%d")} 服侍提醒'

                message.attach(MIMEText(content, 'html'))

                self.send_email(message)

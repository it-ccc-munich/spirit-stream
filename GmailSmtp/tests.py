# Press the green button in the gutter to run the script.
import datetime
from DataTransferObject.ContactDTO import ContactDTO
from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from GmailSmtp.EmailService import EmailService

if __name__ == '__main__':

    email_service = EmailService()

    sundayServiceStaffThisWeek = SundayServiceStaffDTO(datetime.date(2024, 1, 8), "講員名字", "主礼名字", "读经名字", "司琴名字", ["诗歌領唱1", "诗歌領唱2"], "投影名字", "祝福名字", ["儿主帶領1", "儿主帶領2"], ["場地負責1", "場地負責2"], ["接待名字1", "接待名字2"], ["主厨名字", "副厨名字", "采購名字", "幫厨名字"], "團契")
    contactList = [ContactDTO("講員名字", "donin1129@gmail.com")]

    email_service.send_service_reminder_emails(sundayServiceStaffThisWeek, contactList)

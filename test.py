# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import timedelta

from BibleQuery.BibleQuery import BibleQueryService
from DataTransferObject.ContactDTO import ContactDTO
from GmailSmtp.EmailService import EmailService
from GoogleSheets.DateHelper import get_upcoming_sunday
from GoogleSheets.ServiceStaffContactInfoConnector import ServiceStaffContactInfoConnector
from GoogleSheets.SundayServiceSermonScriptureConnector import SundayServiceSermonScriptureConnector
from GoogleSheets.SundayServiceStaffConnector import SundayServiceStaffConnector
from GoogleSheets.SundayServiceStatisticsConnector import SundayServiceStatisticsConnector
from Security.WordPressClient import WorPressClientSecrets
from WordPress.WordPressService import WordPressService


def run():

    # Getbible query service
    bibleQueryService = BibleQueryService()

    # Get connector objects
    sundayServiceStaffConnector = SundayServiceStaffConnector('./Security/church-service-automation-2bbbc534b2e3.json')
    serviceStaffContactInfoConnector = ServiceStaffContactInfoConnector('./Security/church-service-automation-2bbbc534b2e3.json')
    sundayServiceSermonScriptureConnector = SundayServiceSermonScriptureConnector('./Security/church-service-automation-2bbbc534b2e3.json')
    sundayServiceStatisticsConnector = SundayServiceStatisticsConnector('./Security/church-service-automation-2bbbc534b2e3.json')

    # Retrieve data transfer objects
    upcoming_sunday_date = get_upcoming_sunday()
    next_upcoming_sunday_date = upcoming_sunday_date + timedelta(days=7)
    last_sunday_date = upcoming_sunday_date - timedelta(days=7)

    staff_this_week = sundayServiceStaffConnector.get_sunday_service_staff_data(upcoming_sunday_date)
    staff_next_week = sundayServiceStaffConnector.get_sunday_service_staff_data(next_upcoming_sunday_date)

    sermon_and_scripture_last_week = sundayServiceSermonScriptureConnector.get_sermon_scripture_data(last_sunday_date)
    sermon_and_scripture_this_week = sundayServiceSermonScriptureConnector.get_sermon_scripture_data(upcoming_sunday_date)
    sermon_and_scripture_next_week = sundayServiceSermonScriptureConnector.get_sermon_scripture_data(next_upcoming_sunday_date)

    report_last_week = sundayServiceStatisticsConnector.get_service_statistics(last_sunday_date)

    contact_info = serviceStaffContactInfoConnector.get_contact_info_data()

    # For tests, we run everything and most importantly, we only send email to the tester's account, and we set publish_post to false, so it creates a private post
    staff_this_week.projector_operator = "董哲韬"
    contact_info = [ContactDTO("董哲韬", "donin1129@gmail.com")]
    publish_post = False

    # Create the post and this will automatically trigger an email sent to subscribers if publish_post==True
    site_id = 'ccc-munich.org'  # test_site_id = 'testingcccmunich.wordpress.com'
    wordPressService = WordPressService(site_id=site_id,
                                        client_id=WorPressClientSecrets.client_id,
                                        client_secret=WorPressClientSecrets.client_secret,
                                        username=WorPressClientSecrets.username,
                                        password=WorPressClientSecrets.password
                                        )

    post_link = wordPressService.create_post(
        last_week_sunday_service_report=report_last_week,
        this_week_sunday_service_staff=staff_this_week,
        next_week_sunday_service_staff=staff_next_week,

        last_week_sermon_and_scripture=sermon_and_scripture_last_week,
        this_week_sermon_and_scripture=sermon_and_scripture_this_week,
        next_week_sermon_and_scripture=sermon_and_scripture_next_week,

        bible_query_service=bibleQueryService,
        public_post=publish_post
    )

    print(f"WordPress post created with link '{post_link}'")

    # Send email reminder
    email_service = EmailService()
    email_service.send_service_reminder_emails(staff_this_week, sermon_and_scripture_this_week, post_link, contact_info)


if __name__ == '__main__':
    run()

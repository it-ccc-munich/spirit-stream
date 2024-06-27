# Press the green button in the gutter to run the script.
import datetime

from BibleQuery.BibleQuery import BibleQueryService
from DataTransferObject.SundayServiceReportDTO import SundayServiceReportDTO
from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from DataTransferObject.SundayServiceSermonAndScripturesDTO import SundayServiceSermonAndScripturesDTO
from DataTransferObject.VerseDTO import VerseDTO
import WordPressService
from Security.WordPressClient import WorPressClientSecrets

if __name__ == '__main__':

    bibleQueryService = BibleQueryService()

    sundayServiceReport = SundayServiceReportDTO(datetime.date(2024, 1, 1), 80, 20, 50.1)
    sundayServiceStaffThisWeek = SundayServiceStaffDTO(datetime.date(2024, 1, 8),  "主礼名字", "读经名字", "司琴名字", ["诗歌領唱1", "诗歌領唱2"], "投影名字", ["儿主帶領1", "儿主帶領2"], ["場地負責1", "場地負責2"], ["接待名字1", "接待名字2"], ["主厨名字", "副厨名字", "采購名字", "幫厨名字"], "團契")
    sundayServiceReportNextWeek = SundayServiceStaffDTO(datetime.date(2024, 1, 15),  "主礼名字", "读经名字", "司琴名字", ["诗歌領唱1", "诗歌領唱2"], "投影名字", ["儿主帶領1", "儿主帶領2"], ["場地負責1", "場地負責2"], ["接待名字1", "接待名字2"], ["主厨名字", "副厨名字", "采購名字", "幫厨名字"], "團契")
    sundayServiceReportTeachingAndScriptures = SundayServiceSermonAndScripturesDTO(datetime.date(2024, 1, 8), VerseDTO("诗篇", 111, 1), VerseDTO("诗篇", 111, 7), VerseDTO("路加福音", 11, 14), VerseDTO("路加福音", 11, 36), "圣灵的能力", VerseDTO("路加福音", 11, 23))

    # check client info here: https://developer.wordpress.com/apps/
    # create password info here: https://wordpress.com/me/security/two-step
    test_site_id = 'testingcccmunich.wordpress.com'
    site_id = 'ccc-munich.org'
    createPostService = WordPressService.WordPressService(site_id=test_site_id, client_id=WorPressClientSecrets.client_id, client_secret=WorPressClientSecrets.client_secret, username=WorPressClientSecrets.username, password=WorPressClientSecrets.password)
    link = createPostService.create_post(
        last_week_sunday_service_report=sundayServiceReport,
        this_week_sunday_service_staff=sundayServiceStaffThisWeek,
        next_week_sunday_service_staff=sundayServiceReportNextWeek,
        last_week_sermon_and_scripture=sundayServiceReportTeachingAndScriptures,
        this_week_sermon_and_scripture=sundayServiceReportTeachingAndScriptures,
        next_week_sermon_and_scripture=sundayServiceReportTeachingAndScriptures,
        bible_query_service=bibleQueryService,
        public_post=False
    )
    print(link)

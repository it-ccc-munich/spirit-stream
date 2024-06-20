import os

import requests

from BibleQuery.BibleQuery import BibleQueryService
from DataTransferObject import SundayServiceReportDTO, SundayServiceStaffDTO, SundayServiceSermonAndScripturesDTO
from HtmlTemplates import TemplateStringReplacement


class WordPressService:

    def __init__(self, site_id: str, client_id: int, client_secret: str, username: str, password: str):

        self.site_id = site_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password

    def _get_access_token(self):
        token_url = "https://public-api.wordpress.com/oauth2/token"
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        auth_data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'password',
            'username': self.username,
            'password': self.password,
        }
        response = requests.post(token_url, data=auth_data, headers=header)
        assert response.status_code == 200
        return response.json()['access_token']

    def create_post(
            self,
            last_week_sunday_service_report: SundayServiceReportDTO,
            this_week_sunday_service_staff: SundayServiceStaffDTO,
            last_week_sermon_and_scripture: SundayServiceSermonAndScripturesDTO,
            this_week_sermon_and_scripture: SundayServiceSermonAndScripturesDTO,
            next_week_sermon_and_scripture: SundayServiceSermonAndScripturesDTO,
            next_week_sunday_service_staff: SundayServiceStaffDTO,
            bible_query_service: BibleQueryService,
            public_post=False
    ):
        access_token = self._get_access_token()
        url = f"https://public-api.wordpress.com/wp/v2/sites/{self.site_id}/posts"
        header = {'Authorization': f'Bearer {access_token}'}

        filedir = os.path.dirname(__file__)
        weekly_update_template_file = open(os.path.join(filedir, "./WeeklyUpdateTemplate.html"), "r", encoding="utf-8")
        weekly_update_template_content = weekly_update_template_file.read()
        weekly_update_template_file.close()

        golden_verse_template_file = open(os.path.join(filedir, "./GoldenVerseTemplate.html"), "r", encoding="utf-8")
        golden_verse_template_content = golden_verse_template_file.read()
        golden_verse_template_file.close()

        post = {
            'title': f'{this_week_sunday_service_staff.sunday_service_date.strftime("%Y.%m.%d")}教会周报',
            'slug': f'{this_week_sunday_service_staff.sunday_service_date.strftime("%Y-%m-%d")}_info-gottesdienst',
            'categories': [43824102],
            'comment_status': 'closed',
            'ping_status': 'closed',
            'status': 'public' if public_post else 'private',
            'content': TemplateStringReplacement.load_weekly_report_template(
                weekly_update_template_content,
                golden_verse_template_content,
                last_week_sunday_service_report=last_week_sunday_service_report,
                this_week_sunday_service_staff=this_week_sunday_service_staff,

                this_week_sermon_and_scripture=this_week_sermon_and_scripture,
                next_week_sermon_and_scripture=next_week_sermon_and_scripture,
                last_week_golden_verse=last_week_sermon_and_scripture.golden_verse,

                next_week_sunday_service_staff=next_week_sunday_service_staff,
                bible_query_service=bible_query_service
            )
        }
        response = requests.post(url, headers=header, json=post)
        assert response.status_code == 201
        return response.json()['link']

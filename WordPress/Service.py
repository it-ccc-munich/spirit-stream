from typing import Union

import requests

from DataTransferObject import SundayServiceReportDTO, SundayServiceStaffDTO, SundayServiceTeachingAndScripturesDTO
from DataTransferObject.VerseDTO import VerseDTO
import Template


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
            this_week_sunday_service_teaching_and_scripture: SundayServiceTeachingAndScripturesDTO,
            last_week_golden_verse: Union[VerseDTO, None],
            next_week_sunday_service_staff: SundayServiceStaffDTO,
            public_post=False
    ):
        access_token = self._get_access_token()
        url = f"https://public-api.wordpress.com/wp/v2/sites/{self.site_id}/posts"
        header = {'Authorization': f'Bearer {access_token}'}
        post = {
            'title': f'{this_week_sunday_service_staff.sunday_service_date.strftime("%Y.%m.%d")}教会周报',
            'slug': f'{this_week_sunday_service_staff.sunday_service_date.strftime("%Y-%m-%d")}_info-gottesdienst',
            'categories': [43824102],
            'comment_status': 'closed',
            'ping_status': 'closed',
            'status': 'public' if public_post else 'private',
            'content': Template.load_weekly_report_template(
                last_week_sunday_service_report=last_week_sunday_service_report,
                this_week_sunday_service_staff=this_week_sunday_service_staff,
                this_week_sunday_service_teaching_and_scripture=this_week_sunday_service_teaching_and_scripture,
                last_week_golden_verse=last_week_golden_verse,
                next_week_sunday_service_staff=next_week_sunday_service_staff
            )
        }
        response = requests.post(url, headers=header, json=post)
        assert response.status_code == 201
        return response.json()['link']

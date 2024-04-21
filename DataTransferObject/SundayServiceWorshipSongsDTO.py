from datetime import date
from WorshipSongDTO import WorshipSongDTO


class SundayServiceWorshipSongsDTO:
    def __init__(self, sunday_service_date: date,
                 first: WorshipSongDTO,
                 second: WorshipSongDTO,
                 third: WorshipSongDTO):

        # 日期
        self.sunday_service_date = sunday_service_date
        # 第一首
        self.first = first
        # 第二首
        self.second = second
        # 第三首/回应诗歌
        self.third = third

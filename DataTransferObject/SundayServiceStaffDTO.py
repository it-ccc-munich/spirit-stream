from datetime import date
from typing import List


class SundayServiceStaffDTO:
    def __init__(self, sunday_service_date: date, host: str, scripture_reader: str, pianist: str,
                 hymn_leaders: List[str], projector_operator: str,
                 sunday_school_leaders: List[str], venue: List[str], greeters: List[str],
                 meal_preparers: List[str], fellowship: str):

        # 日期
        self.sunday_service_date = sunday_service_date
        # 主礼
        self.host = host
        # 读经
        self.scripture_reader = scripture_reader
        # 司琴
        self.pianist = pianist
        # 诗歌
        self.hymn_leaders = hymn_leaders
        # 投影
        self.projector_operator = projector_operator
        # 儿主
        self.sunday_school_leaders = sunday_school_leaders
        # 场地
        self.venue = venue
        # 接待
        self.greeters = greeters
        # 饭食
        self.meal_preparers = meal_preparers
        # 司事
        self.fellowship = fellowship

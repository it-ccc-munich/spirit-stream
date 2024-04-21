from datetime import date
from typing import List


class SundayServiceStaffDTO:
    def __init__(self, sunday_service_date: date, preacher: str, host: str, scripture_reader: str, pianist: str,
                 hymn_leaders: List[str], projector_operator: str, benediction: str,
                 sunday_school_activity: str, venue: List[str], greeters: str,
                 meal_preparers: List[str], fellowship: str):

        # 日期
        self.sunday_service_date = sunday_service_date
        # 讲员
        self.preacher = preacher
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
        # 祝福
        self.benediction = benediction
        # 儿主
        self.sunday_school_activity = sunday_school_activity
        # 场地
        self.venue = venue
        # 接待
        self.greeters = greeters
        # 饭食
        self.meal_preparers = meal_preparers
        # 司事
        self.fellowship = fellowship

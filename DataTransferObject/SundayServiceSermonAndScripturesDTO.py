from datetime import date
from typing import Union

from .VerseDTO import VerseDTO


class SundayServiceSermonAndScripturesDTO:
    def __init__(self, sunday_service_date: date, preacher: str,
                 psalms_of_inspiration_start: VerseDTO, psalms_of_inspiration_end: VerseDTO,
                 scripture_start: VerseDTO, scripture_end: VerseDTO,
                 teaching_title: str, benediction: str,
                 golden_verse: Union[VerseDTO, None]):

        # 日期
        self.sunday_service_date = sunday_service_date
        # 讲员
        self.preacher = preacher
        # 启应诗篇(开始)
        self.psalms_of_inspiration_start = psalms_of_inspiration_start
        # 启应诗篇(结束)
        self.psalms_of_inspiration_end = psalms_of_inspiration_end
        # 经文(开始)
        self.scripture_start = scripture_start
        # 经文(结束)
        self.scripture_end = scripture_end
        # 题目
        self.teaching_title = teaching_title
        # 祝福
        self.benediction = benediction
        # 金句
        # TODO: 需要考慮多條經文的金句嗎？
        self.golden_verse = golden_verse

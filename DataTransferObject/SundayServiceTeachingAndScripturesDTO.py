from datetime import date
from VerseDTO import VerseDTO


class SundayServiceTeachingAndScripturesDTO:
    def __init__(self, sunday_service_date: date,
                 psalms_of_inspiration_start: VerseDTO, psalms_of_inspiration_end: VerseDTO,
                 scripture_start: VerseDTO, scripture_end: VerseDTO,
                 teaching_title: str,
                 golden_verse: VerseDTO):

        # 日期
        self.sunday_service_date = sunday_service_date
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
        # 金句
        # TODO: 需要考慮多條經文的金句嗎？
        self.golden_verse = golden_verse

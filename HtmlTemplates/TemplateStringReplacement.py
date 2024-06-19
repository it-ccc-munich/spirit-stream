from typing import Union

from BibleQuery.BibleQuery import BibleQueryService
from DataTransferObject.SundayServiceReportDTO import SundayServiceReportDTO
from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from DataTransferObject.SundayServiceSermonAndScripturesDTO import SundayServiceSermonAndScripturesDTO
from DataTransferObject.VerseDTO import format_scripture_abbreviation, VerseDTO


def load_weekly_report_template(
    weekly_report_template: str,
    golden_verse_template: str,
    last_week_sunday_service_report: SundayServiceReportDTO,
    this_week_sunday_service_staff: SundayServiceStaffDTO,
    this_week_sermon_and_scripture: SundayServiceSermonAndScripturesDTO,
    next_week_sermon_and_scripture: SundayServiceSermonAndScripturesDTO,
    last_week_golden_verse: Union[VerseDTO, None],
    next_week_sunday_service_staff: SundayServiceStaffDTO,
    bible_query_service: BibleQueryService
):

    # 上周汇报
    weekly_report_template = weekly_report_template.replace('%LAST_SERVICE_MONTH%', f"{last_week_sunday_service_report.sunday_service_date.month}")
    weekly_report_template = weekly_report_template.replace('%LAST_SERVICE_DATE%', f"{last_week_sunday_service_report.sunday_service_date.day}")
    weekly_report_template = weekly_report_template.replace('%LAST_SERVICE_ATTENDED_ADULTS%', f"{last_week_sunday_service_report.adults_attended}")
    weekly_report_template = weekly_report_template.replace('%LAST_SERVICE_ATTENDED_CHILDREN%', f"{last_week_sunday_service_report.children_attended}")
    weekly_report_template = weekly_report_template.replace('%LAST_SERVICE_OFFERING%', f"{last_week_sunday_service_report.offering}")

    weekly_report_template = replace_this_week_service_staff(weekly_report_template, this_week_sunday_service_staff, this_week_sermon_and_scripture)

    # 主日教导和经文
    weekly_report_template = weekly_report_template.replace('%THIS_SERVICE_PSALMS%', f"{format_scripture_abbreviation(this_week_sermon_and_scripture.psalms_of_inspiration_start, this_week_sermon_and_scripture.psalms_of_inspiration_end)}")
    weekly_report_template = weekly_report_template.replace('%THIS_SERVICE_SCRIPTURE%', f"{format_scripture_abbreviation(this_week_sermon_and_scripture.scripture_start, this_week_sermon_and_scripture.scripture_end)}")
    weekly_report_template = weekly_report_template.replace('%THIS_SERVICE_TEACHING_TITLE%', f"{this_week_sermon_and_scripture.teaching_title}")

    # 上周金句
    if last_week_golden_verse:
        weekly_report_template = weekly_report_template.replace('%LAST_SERVICE_GOLDEN_VERSE_SECTION%', load_golden_verse_section_template(golden_verse_template, "上周金句：", last_week_golden_verse, bible_query_service))
    # 本周金句
    if this_week_sermon_and_scripture.golden_verse:
        weekly_report_template = weekly_report_template.replace('%THIS_SERVICE_GOLDEN_VERSE_SECTION%', load_golden_verse_section_template(golden_verse_template, "本周金句：", this_week_sermon_and_scripture.golden_verse, bible_query_service))

    # 下周服事人员
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_PREACHER%', f"{next_week_sermon_and_scripture.preacher}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_HOST%', f"{next_week_sunday_service_staff.host}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_SCRIPTURE_READER%', f"{next_week_sunday_service_staff.scripture_reader}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_PIANIST%', f"{next_week_sunday_service_staff.pianist}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_HYMN_LEADERS%', f"{'，'.join(next_week_sunday_service_staff.hymn_leaders)}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_PROJECTOR_OPERATOR%', f"{next_week_sunday_service_staff.projector_operator}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_BENEDICTION%', f"{next_week_sermon_and_scripture.benediction}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_SUNDAY_SCHOOL_LEADERS%', f"{'，'.join(next_week_sunday_service_staff.sunday_school_leaders)}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_VENUE%', f"{'，'.join(next_week_sunday_service_staff.venue)}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_GREETERS%', f"{'，'.join(next_week_sunday_service_staff.greeters)}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_MEAL_PREPARERS%', f"{'，'.join(next_week_sunday_service_staff.meal_preparers)}")
    weekly_report_template = weekly_report_template.replace('%NEXT_SERVICE_FELLOWSHIP%', f"{next_week_sunday_service_staff.fellowship}")

    # 奉献金句
    weekly_report_template = weekly_report_template.replace('%OFFERING_GOLDEN_VERSE_SECTION%', load_golden_verse_section_template_from_str("奉献金句：", "37. 主耶和华如此说，我要加增以色列家的人数，多如羊群。他们必为这事向我求问，我要给他们成就。<br>38. 耶路撒冷在守节作祭物所献的羊群怎样多，照样，荒凉的城邑必被人群充满。他们就知道我是耶和华。", "以西结书 36:37-38"))

    return weekly_report_template


def replace_this_week_service_staff(content: str, this_week_sunday_service_staff: SundayServiceStaffDTO, this_week_sermon_and_scripture: SundayServiceSermonAndScripturesDTO):

    # 本周服事人员
    content = content.replace('%THIS_SERVICE_PREACHER%', f"{this_week_sermon_and_scripture.preacher}")
    content = content.replace('%THIS_SERVICE_HOST%', f"{this_week_sunday_service_staff.host}")
    content = content.replace('%THIS_SERVICE_SCRIPTURE_READER%', f"{this_week_sunday_service_staff.scripture_reader}")
    content = content.replace('%THIS_SERVICE_PIANIST%', f"{this_week_sunday_service_staff.pianist}")
    content = content.replace('%THIS_SERVICE_HYMN_LEADERS%', f"{'，'.join(this_week_sunday_service_staff.hymn_leaders)}")
    content = content.replace('%THIS_SERVICE_PROJECTOR_OPERATOR%', f"{this_week_sunday_service_staff.projector_operator}")
    content = content.replace('%THIS_SERVICE_BENEDICTION%', f"{this_week_sermon_and_scripture.benediction}")
    content = content.replace('%THIS_SERVICE_SUNDAY_SCHOOL_LEADERS%', f"{'，'.join(this_week_sunday_service_staff.sunday_school_leaders)}")
    content = content.replace('%THIS_SERVICE_VENUE%', f"{'，'.join(this_week_sunday_service_staff.venue)}")
    content = content.replace('%THIS_SERVICE_GREETERS%', f"{'，'.join(this_week_sunday_service_staff.greeters)}")
    content = content.replace('%THIS_SERVICE_MEAL_PREPARERS%', f"{'，'.join(this_week_sunday_service_staff.meal_preparers)}")
    content = content.replace('%THIS_SERVICE_FELLOWSHIP%', f"{this_week_sunday_service_staff.fellowship}")

    return content


def load_golden_verse_section_template(golden_verse_template: str, title: str, golden_verse: VerseDTO, bible_query_service: BibleQueryService):
    # golden_verse_file = open("../WordPress/GoldenVerseTemplate.html", "r", encoding="utf-8")
    # golden_verse_section = golden_verse_file.read()
    # golden_verse_file.close()

    text = bible_query_service.get_verses([golden_verse])[0]

    golden_verse_template = golden_verse_template.replace('%TITLE%', title)
    golden_verse_template = golden_verse_template.replace('%CONTENT%', text)
    golden_verse_template = golden_verse_template.replace('%ABBREVIATION%', f"{golden_verse.book} {golden_verse.chapter}:{golden_verse.verse}")

    return golden_verse_template


def load_golden_verse_section_template_from_str(golden_verse_template: str, title: str, content: str, abbreviation: str):
    # golden_verse_file = open("../WordPress/GoldenVerseTemplate.html", "r", encoding="utf-8")
    # golden_verse_section = golden_verse_file.read()
    # golden_verse_file.close()

    golden_verse_template = golden_verse_template.replace('%TITLE%', title)
    golden_verse_template = golden_verse_template.replace('%CONTENT%', content)
    golden_verse_template = golden_verse_template.replace('%ABBREVIATION%', abbreviation)

    return golden_verse_template

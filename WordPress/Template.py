from typing import Union

from DataTransferObject.SundayServiceReportDTO import SundayServiceReportDTO
from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO
from DataTransferObject.SundayServiceTeachingAndScripturesDTO import SundayServiceTeachingAndScripturesDTO
from DataTransferObject.VerseDTO import format_scripture_abbreviation, VerseDTO


def load_weekly_report_template(
    last_week_sunday_service_report: SundayServiceReportDTO,
    this_week_sunday_service_staff: SundayServiceStaffDTO,
    this_week_sunday_service_teaching_and_scripture: SundayServiceTeachingAndScripturesDTO,
    last_week_golden_verse: Union[VerseDTO, None],
    next_week_sunday_service_staff: SundayServiceStaffDTO
):
    file = open("./WeeklyUpdateTemplate.html", "r", encoding="utf-8")
    content = file.read()
    file.close()

    # 上周汇报
    content = content.replace('%LAST_SERVICE_MONTH%', f"{last_week_sunday_service_report.sunday_service_date.month}")
    content = content.replace('%LAST_SERVICE_DATE%', f"{last_week_sunday_service_report.sunday_service_date.day}")
    content = content.replace('%LAST_SERVICE_ATTENDED_ADULTS%', f"{last_week_sunday_service_report.adults_attended}")
    content = content.replace('%LAST_SERVICE_ATTENDED_CHILDREN%', f"{last_week_sunday_service_report.children_attended}")
    content = content.replace('%LAST_SERVICE_OFFERING%', f"{last_week_sunday_service_report.offering}")

    # 本周服事人员
    content = content.replace('%THIS_SERVICE_PREACHER%', f"{this_week_sunday_service_staff.preacher}")
    content = content.replace('%THIS_SERVICE_HOST%', f"{this_week_sunday_service_staff.host}")
    content = content.replace('%THIS_SERVICE_SCRIPTURE_READER%', f"{this_week_sunday_service_staff.scripture_reader}")
    content = content.replace('%THIS_SERVICE_PIANIST%', f"{this_week_sunday_service_staff.pianist}")
    content = content.replace('%THIS_SERVICE_HYMN_LEADERS%', f"{'，'.join(this_week_sunday_service_staff.hymn_leaders)}")
    content = content.replace('%THIS_SERVICE_PROJECTOR_OPERATOR%', f"{this_week_sunday_service_staff.projector_operator}")
    content = content.replace('%THIS_SERVICE_BENEDICTION%', f"{this_week_sunday_service_staff.benediction}")
    content = content.replace('%THIS_SERVICE_SUNDAY_SCHOOL_LEADERS%', f"{'，'.join(this_week_sunday_service_staff.sunday_school_leaders)}")
    content = content.replace('%THIS_SERVICE_VENUE%', f"{'，'.join(this_week_sunday_service_staff.venue)}")
    content = content.replace('%THIS_SERVICE_GREETERS%', f"{'，'.join(this_week_sunday_service_staff.greeters)}")
    content = content.replace('%THIS_SERVICE_MEAL_PREPARERS%', f"{'，'.join(this_week_sunday_service_staff.meal_preparers)}")
    content = content.replace('%THIS_SERVICE_FELLOWSHIP%', f"{this_week_sunday_service_staff.fellowship}")

    # 主日教导和经文
    content = content.replace('%THIS_SERVICE_PSALMS%', f"{format_scripture_abbreviation(this_week_sunday_service_teaching_and_scripture.psalms_of_inspiration_start, this_week_sunday_service_teaching_and_scripture.psalms_of_inspiration_end)}")
    content = content.replace('%THIS_SERVICE_SCRIPTURE%', f"{format_scripture_abbreviation(this_week_sunday_service_teaching_and_scripture.scripture_start, this_week_sunday_service_teaching_and_scripture.scripture_end)}")
    content = content.replace('%THIS_SERVICE_TEACHING_TITLE%', f"{this_week_sunday_service_teaching_and_scripture.teaching_title}")

    # 上周金句
    if last_week_golden_verse:
        content = content.replace('%LAST_SERVICE_GOLDEN_VERSE_SECTION%', load_golden_verse_section_template("上周金句：", last_week_golden_verse))
    # 本周金句
    if this_week_sunday_service_teaching_and_scripture.golden_verse:
        content = content.replace('%THIS_SERVICE_GOLDEN_VERSE_SECTION%', load_golden_verse_section_template("本周金句：", this_week_sunday_service_teaching_and_scripture.golden_verse))

    # 下周服事人员
    content = content.replace('%NEXT_SERVICE_PREACHER%', f"{next_week_sunday_service_staff.preacher}")
    content = content.replace('%NEXT_SERVICE_HOST%', f"{next_week_sunday_service_staff.host}")
    content = content.replace('%NEXT_SERVICE_SCRIPTURE_READER%', f"{next_week_sunday_service_staff.scripture_reader}")
    content = content.replace('%NEXT_SERVICE_PIANIST%', f"{next_week_sunday_service_staff.pianist}")
    content = content.replace('%NEXT_SERVICE_HYMN_LEADERS%', f"{'，'.join(next_week_sunday_service_staff.hymn_leaders)}")
    content = content.replace('%NEXT_SERVICE_PROJECTOR_OPERATOR%', f"{next_week_sunday_service_staff.projector_operator}")
    content = content.replace('%NEXT_SERVICE_BENEDICTION%', f"{next_week_sunday_service_staff.benediction}")
    content = content.replace('%NEXT_SERVICE_SUNDAY_SCHOOL_LEADERS%', f"{'，'.join(next_week_sunday_service_staff.sunday_school_leaders)}")
    content = content.replace('%NEXT_SERVICE_VENUE%', f"{'，'.join(next_week_sunday_service_staff.venue)}")
    content = content.replace('%NEXT_SERVICE_GREETERS%', f"{'，'.join(next_week_sunday_service_staff.greeters)}")
    content = content.replace('%NEXT_SERVICE_MEAL_PREPARERS%', f"{'，'.join(next_week_sunday_service_staff.meal_preparers)}")
    content = content.replace('%NEXT_SERVICE_FELLOWSHIP%', f"{next_week_sunday_service_staff.fellowship}")

    # 奉献金句
    content = content.replace('%OFFERING_GOLDEN_VERSE_SECTION%', load_golden_verse_section_template_from_str("奉献金句：", "37. 主耶和华如此说，我要加增以色列家的人数，多如羊群。他们必为这事向我求问，我要给他们成就。<br>38. 耶路撒冷在守节作祭物所献的羊群怎样多，照样，荒凉的城邑必被人群充满。他们就知道我是耶和华。", "以西结书 36:37-38"))

    return content


def load_golden_verse_section_template(title: str, golden_verse: VerseDTO):
    golden_verse_file = open("./GoldenVerseTemplate.html", "r", encoding="utf-8")
    golden_verse_section = golden_verse_file.read()
    golden_verse_file.close()

    golden_verse_section = golden_verse_section.replace('%TITLE%', title)
    golden_verse_section = golden_verse_section.replace('%CONTENT%', "新深検蜂止前問扱海克気他見社要働口塚。月手浪税問国寿迎続省己維曲創三除坂。日隅達家州関応写能財消阪藤半東在問。")  # TODO: add verse query
    golden_verse_section = golden_verse_section.replace('%ABBREVIATION%', f"{golden_verse.book} {golden_verse.chapter}:{golden_verse.verse}")

    return golden_verse_section


def load_golden_verse_section_template_from_str(title: str, content: str, abbreviation: str):
    golden_verse_file = open("./GoldenVerseTemplate.html", "r", encoding="utf-8")
    golden_verse_section = golden_verse_file.read()
    golden_verse_file.close()

    golden_verse_section = golden_verse_section.replace('%TITLE%', title)
    golden_verse_section = golden_verse_section.replace('%CONTENT%', content)
    golden_verse_section = golden_verse_section.replace('%ABBREVIATION%', abbreviation)

    return golden_verse_section

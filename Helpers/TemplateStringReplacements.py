from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO


def replace_this_week_service_staff(content: str, this_week_sunday_service_staff: SundayServiceStaffDTO):

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

    return content

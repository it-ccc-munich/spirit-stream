import re
from datetime import datetime

from gspread import Worksheet

from DataTransferObject.SundayServiceStaffDTO import SundayServiceStaffDTO


def chinese2datetime(chinese_text):
    # for converting chinese text to datetime
    # author : simon

    transformed_dates = []

    pattern = r'(\d{1,2})月(\d{1,2})日'
    for chinese_date in chinese_text:
        matched = re.match(pattern, chinese_date)
        if matched:
            year = 2024
            month = int(matched.group(1))
            day = int(matched.group(2))
            transformed_dates.append(datetime(year, month, day))
        else:
            transformed_dates.append(None)

    return transformed_dates


def find_date_index(target_date: datetime.date, worksheet: Worksheet):
    # find target row in the worksheet according to date
    # author: simon

    # Specify the column you want to read (column A is 1, B is 2, etc.)
    column_index = 1  # for date column
    date_column_chinese = worksheet.col_values(column_index)
    date_in_chinese = f"{str(target_date.month).zfill(2)}月{str(target_date.day).zfill(2)}日"
    try:
        return date_column_chinese.index(date_in_chinese)
    except ValueError:
        print("Did not find th entry for the target date in google sheets")
        return None


def read_sunday_service_staff(row_index, worksheet: Worksheet):
    # extract information from 同工表 and save in a dictionary
    # e.g., {"场地": Name}
    # author ：jiawen

    # 服侍岗位列表
    positions_names = ["讲员", "主礼", "PPT制作", "主领", "副领", "司琴", "场地1", "场地2", "儿主大班", "儿主小班", "小班助教", "成人基要班", "饭食采购", "主厨", "帮厨1", "帮厨2", "餐后打扫"]
    #  one extra column for 日期
    num_columns = len(positions_names) + 1
    dict_for_row = {}

    # TODO: Improve performance with row based query
    for column_index in range(2, num_columns + 1):
        # skip the first column which is the date
        column_values = worksheet.col_values(column_index)
        # here is very hard-coding
        column_title = column_values[1]
        # assert column_title not in positions_names, "请更新服侍岗位列表!"

        if len(column_values) <= row_index:
            dict_for_row[column_title] = ""
            continue

        target_column_value = column_values[row_index]
        dict_for_row[column_title] = target_column_value

    return dict_for_row


def dict2dto(target_date, result_dict):
    # jiawen, for weekly report

    return SundayServiceStaffDTO(
        sunday_service_date=target_date,
        preacher=result_dict['讲员'],
        host=result_dict['主礼'],
        scripture_reader=result_dict['主礼'],
        pianist=result_dict['司琴'],
        hymn_leaders=[result_dict['主领'], result_dict['副领']],
        projector_operator=result_dict['PPT制作'],
        benediction='',
        sunday_school_leaders=[result_dict['儿主大班'], result_dict['儿主小班']],
        venue=[result_dict['场地1'], result_dict['场地2']],
        greeters=[],
        meal_preparers=[result_dict['饭食采购'], result_dict['主厨'], result_dict['帮厨1'], result_dict['帮厨2']],
        fellowship=result_dict['餐后打扫']
    )

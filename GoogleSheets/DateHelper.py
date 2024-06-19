import re
from datetime import datetime, timedelta

from gspread import Worksheet


def get_upcoming_sunday() -> datetime.date:
    # Obtain this upcoming sunday date
    today = datetime.today()
    days_until_sunday = (6 - today.weekday()) % 7  # Calculate the number of days until Sunday
    date_this_sunday = today + timedelta(days=days_until_sunday)  # Add the number of days until Sunday
    return date_this_sunday.date()


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
        return date_column_chinese.index(date_in_chinese) + 1
    except ValueError:
        print("Did not find th entry for the target date in google sheets")
        return None
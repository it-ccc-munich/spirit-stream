from datetime import datetime, timedelta


def get_upcoming_sunday() -> datetime.date:
    # Obtain this upcoming sunday date
    today = datetime.today()
    days_until_sunday = (6 - today.weekday()) % 7  # Calculate the number of days until Sunday
    date_this_sunday = today + timedelta(days=days_until_sunday)  # Add the number of days until Sunday
    return date_this_sunday.date()

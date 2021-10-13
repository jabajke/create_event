from datetime import datetime, timedelta

date_in_7_days = datetime.now() + timedelta(days=7)

print(date_in_7_days.time())

print(datetime(year=date_in_7_days.year, month=date_in_7_days.month, day=date_in_7_days.day, hour=18))

import calendar

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return calendar.day_name[calendar.weekday(year, month, day)]
    
# import datetime, calendar
# class Solution:
#     def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
# 		x = datetime.datetime(year, month, day).weekday()
# 		return str(calendar.day_name[x])

# return date(year, month, day).strftime("%A")

# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

if __name__ == "__main__":
    month, day, year = map(str, input().split())
    month = int(month)
    day = int(day)
    year = int(year)
    
    week_day = calendar.weekday(year, month, day)
    result = calendar.day_name[week_day].upper()
    print(result)

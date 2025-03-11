import calendar

if __name__ == '__main__':
    try:
        month, day, year = map(int, input().split())
    except ValueError:
        print(ValueError)
    day_idx = calendar.weekday(year, month, day)

    day = calendar.day_name[day_idx]
    print(day.upper())

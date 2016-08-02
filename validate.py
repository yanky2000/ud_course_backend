months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
months_abbr = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower() #if first 3 correct the user is on the right track
        print(months_abbr.get(short_month)) # Use print because I can't see return in output
        return months_abbr.get(short_month)

# valid_month('deca')
# valid_month('december')


def valid_day(day):
    if day and day.isdigit(): #First check if day consists of digits only
        day = int(day)
        if 0 < day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit(): #First check if year consists of digits only
        year = int(year)
        if 0 < year <= 31:
            return year

# print(valid_day('3'))
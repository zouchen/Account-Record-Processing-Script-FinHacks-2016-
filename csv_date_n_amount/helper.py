import csv, codecs
from datetime import date, datetime, timedelta



# helper function
def perdelta(start, end, delta):
    curr = start
    while curr <= end:
        yield curr
        curr += delta


# helper function
# dataPeriod(y1, m1, d1, y2, m2, d2) returns a list of all dates in the period.
# dataPeriod: Int Int Int Int Int Int -> (lstof Str)
def dataPeriod(y1, m1, d1, y2, m2, d2):
    period = []
    for each in perdelta(date(y1, m1, d1), date(y2, m2, d2), timedelta(days=1)):
        y = str(each.year)
        if each.month < 10:
            m = '0' + str(each.month)
        else: 
            m = str(each.month)
        if each.day < 10:
            d = '0' + str(each.day)
        else: 
            d = str(each.day)
        period.append(y + '-' + m + '-' + d)
    return period


# helper function
def CurrentMonth(month):
    if month <= 9:
        return '0' + str(month)
    else:
        return str(month)    


# helper function
def LastMonth(month):
    if month <= 10:
        return '0' + str(month - 1)
    else:
        return str(month - 1)
  
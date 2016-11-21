import csv, codecs, helper
from datetime import date, datetime, timedelta
# from tabulate import tabulate


# import pandas as pd
# rng = pd.date_range('2012-01-01', '2012-01-03')
# rng1 = pd.date_range('2016-08-29', periods=7, freq='D')



# TotS(fileName, y1, m1, d1, y2, m2, d2) return the total spending amount in the period.
# TotS: Str, Int, Int, Int, Int, Int, Int -> Int
def TotS(fileName, y1, m1, d1, y2, m2, d2):
    total = 0
    period = helper.dataPeriod(y1, m1, d1, y2, m2, d2)

    f = open(fileName)
    csvReader = csv.reader(codecs.open(fileName, 'rU'))

    for row in csvReader:
        if row[0] in period and row[2] != '':
            total += float(row[2])

    f.close
    return total



def res(sy, sm, sd, ey, em, ed):
    return TotS('cibccreditcard_2015.csv', sy, sm, sd, ey, em, ed)



if __name__ == "__main__":
    print(res(2016, 8, 1, 2016, 9, 30))



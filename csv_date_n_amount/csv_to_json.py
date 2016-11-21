import csv
import json

csvfile = open('cibccreditcard_2015.csv', 'r')
jsonfile = open('cibccreditcard_2015.json', 'w')

fieldnames = ("Date","Business","Debit","Credit")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')


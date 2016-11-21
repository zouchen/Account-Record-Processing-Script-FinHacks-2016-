import csv, json, time
from pprint import pprint
import csv_to_json as ctj
import csvReader



def data():
    
    with open('LocationHistory.json') as read:    
        data = json.load(read)
    return(data)


def cato():
    locations = {}
    
    for each in data()['locations']:
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(each['timestampMs'])/1000))[:10]
        if len(date) == 10:
            locations[date] = []
    
    for each in data()['locations']:
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(each['timestampMs'])/1000))[:10]
        if len(date) == 10:
            locations[date].append('{0}, {1}'.format(each['latitudeE7'], each['longitudeE7']))
        
    for each in locations:
        locations[each] = list(set(locations[each]))
        
    return(locations)



def output_csv(dic):
    with open('LocationHistory.csv', 'w') as csvfile:
        fieldnames = ['Date', 'Locations', 'Spending']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for each in dic:
            spending = csvReader.res(int(each[0:4]), int(each[5:7]), int(each[8:10]), int(each[0:4]), int(each[5:7]), int(each[8:10]))
            if spending != 0:
                writer.writerow({'Date': each, 'Locations': dic[each], 'Spending': spending})



def filtered_json():
    output_csv(cato())
    csvfile = open('LocationHistory.csv', 'r')
    jsonfile = open('merged.json', 'w')
    
    fieldnames = ("Date", "Locations", "Spending")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')    


# import brewery.ds as ds
import sys



def merge():
    
    f1 = open("cibccreditcard_2015.csv")
    f2 = open("LocationHistory_filtered.csv")
    csv1 = csv.reader(codecs.open("cibccreditcard_2015.csv", 'rU'))
    csv2 = csv.reader(codecs.open("LocationHistory_filtered.csv", 'rU'))

    for row in csv1:
        if row[0] in period and row[2] != '':
            total += float(row[2])

    f.close


'''
fout=open("out.csv","a")
# first file:
for line in open("cibccreditcard_2015.csv"):
    fout.write(line)
# now the rest:    
for num in range(2,201):
    f = open("sh"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
'''



'''
sources = [
    {"name": "cibccreditcard_2015.csv", "fields": ["Date", "Credit", "Business", "Debit"]},
    {"name": "LocationHistory_filtered.csv", "fields": ["Date", "Locations"]}
]


# We want to store filename as origin of each row
all_fields = ["file"]

# Go through source definitions and collect the fields
for source in sources:
    fields = source.get("fields")
    for field in fields:
        if field not in all_fields:
            all_fields.append(field)
            
            
out = ds.CSVDataTarget("merged.csv")
out.fields = ds.fieldlist(all_fields)
out.initialize()



for source in sources:
    path = source["path"]
    fields = source.get("fields")

    # Initialize data source: skip reading of headers - we are preparing them ourselves
    # use XLSDataSource for XLS files
    src = ds.CSVDataSource(path, read_header = False)
    src.fields = ds.fieldlist(fields)
    src.initialize()

    for record in src.records():

        # Add file reference into ouput - to know where the row comes from
        record["file"] = path
        out.append(record)

    # Close the source stream
    src.finalize()
'''
    

'''
out = ds.YamlDirectoryDataTarget("merged_grants")


out = ds.SQLDataTarget(url = "postgres://localhost/opendata",
                       table = "grants",
                       truncate = True)
'''




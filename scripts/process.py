import csv
from datetime import datetime

r = csv.reader(open("source.csv","r"), delimiter = ',')
header = next(r)
header1 = ['year','month','day', 'region','value']
with open('result.csv','w') as result:
    writer = csv.writer(result, lineterminator='\n')
    writer.writerow(header1)
    for row in r:
        yy = datetime.strptime(row[0],'%Y-%m-%d').strftime('%Y')
        mm = datetime.strptime(row[0],'%Y-%m-%d').strftime('%B')
        dd = datetime.strptime(row[0],'%Y-%m-%d').strftime('%a')
        writer.writerow((yy,mm,dd,row[1],row[2]))
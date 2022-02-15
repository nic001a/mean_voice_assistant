import csv

with open('curse_eng.csv') as csv_file:
    csv_read= csv.reader(csv_file)
    for row in csv_read :
       # print(row[0])
        print ( len(row))
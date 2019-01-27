import csv

results = []
with open('resale-flat-prices.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    results = [row for row in reader if row[2] == '3 ROOM' and row[7] == 'ADJOINED FLAT']

with open('q1.csv', 'w') as csvWriter:
    writer = csv.writer(csvWriter)
    writer.writerows(results)

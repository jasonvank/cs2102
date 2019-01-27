import csv

results = []
with open('resale-flat-prices.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    # results = [int(round(row[6]*1.1)) for row in reader if row[1] == 'YISHUN']
    for row in reader:
        if row[1] == 'YISHUN':
            row[6] = int(row[6]) * 1.1
        results.append(row)

with open('q5.csv', 'w') as csvWriter:
    writer = csv.writer(csvWriter)
    writer.writerows(results)

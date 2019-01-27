import csv
import itertools
import math

results = []
with open('resale-flat-prices.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    curGroup = []
    results = []
    for key, group in itertools.groupby(sorted(reader, key = lambda x: x[1]), lambda i: i[1]):
        curGroup = list(group)

        # cumPsm, maxPsm, minPsm = 0, 0, 100000
        # numOfTransaction = len(curGroup)
        if key == 'BISHAN':
            for group in curGroup: 
                print(group)
                # print(group)
                # try:
                # curPsm = int(math.ceil(float(group[9]) / float(group[6])))
                # cumPsm = cumPsm + curPsm
                # maxPsm = max(maxPsm, curPsm)
                # minPsm = min(minPsm, curPsm)
                # except:
            #     print(group[9] + group[6] + '*')
            #     break
        # results.append([key, numOfTransaction, maxPsm, int(math.ceil(cumPsm/numOfTransaction)), minPsm])

results.sort(key = lambda x : x[3], reverse=True)

with open('q3.csv', 'w') as csvWriter:
    writer = csv.writer(csvWriter)
    writer.writerows(results)

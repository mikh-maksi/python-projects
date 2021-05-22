import csv

with open('c:\work\python\data\data.csv') as f:
    reader = csv.reader(f,delimiter = ";")
    c = 0
    # print(reader)
    for row in reader:
        s = 0
        lst = []
        for i in range(len(row)):
            if i>0:
                lst.append(float(row[i]))
        print(row[0],sum(lst),max(lst),min(lst),sum(lst)/len(lst))

        
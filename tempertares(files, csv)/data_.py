import csv

with open('c:\work\python\data\data.csv') as f:
    reader = csv.reader(f,delimiter = ";")
    c = 0
    # print(reader)
    for row in reader:
        s = 0
        lst = []
        for i in row:
            lst.append(float(i))
        print(sum(lst))
        print(len(lst))
        print(max(lst))
        print(min(lst))
        print(sum(lst)/len(lst))

        
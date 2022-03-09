import os
import csv

data = []
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        filename = row[1]
        timestamp = row[0]
        timeval = str(int(10**9 * float(timestamp)))
        os.rename("data/" + filename, "data/" + timeval + ".png")
        data.append([timeval, timeval + ".png"])

with open("data2.csv", "w") as file:
    writer = csv.writer(file)
    while(len(data) != 0):
        writer.writerow(data[0])
        data.pop(0)
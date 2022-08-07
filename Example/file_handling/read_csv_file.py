import csv

file = open('exFiles/data.csv')  # With header
file2 = open('exFiles/data2.csv')  # Without header

csvCursor = csv.reader(file)
csvCursor2 = csv.reader(file2)

for row in csvCursor2:
    print(f"{row[0]} \t|\t {row[2]}")

file.close()
import csv

file = open('data.csv')  # With header
file2 = open('data2.csv')  # Without header

csvCursor = csv.reader(file)
csvCursor2 = csv.reader(file2)

for row in csvCursor2:
    print(f"{row[0]} \t|\t {row[2]}")

file.close()
import csv

file = open('exFiles/data2.csv')  # Without header
fields = ["Name", "Gender", "Score", "Age", "AgeStage", "Birthday"]

csvCursor = csv.DictReader(file, fields)

for row in csvCursor:
    print(f"{row['Name']} \t|\t {row['Score']} \t|\t {row['Gender']}")

file.close()
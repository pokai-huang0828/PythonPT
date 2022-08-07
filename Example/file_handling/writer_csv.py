import csv

header = ['Name', 'Address', 'Phone', 'Email', 'Age']
data = [
    ["Sean", "123, Oak Street, Taipei", "02-9876-5432", "sean@gmail.com", 40],
    ["Amy", "456, Park Avenue, Taichung", "04-8877-6655", "amy@gmail.com", 30],
    ["David", "789 First Road Tainan", "06-654-3210", "david@gmail.com", 25]
]

f = open("exFiles/contact2.csv", "w")
csvCursor = csv.writer(f, dialect='excel-tab')   # dialect：指定特定CSV方言(一組的格式參數設定)
csvCursor.writerow(header)

for d in data:
    csvCursor.writerow(d)

f.close()
print("Data has output in to contact.csv")
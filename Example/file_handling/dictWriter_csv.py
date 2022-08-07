import csv

header = ['Name', 'Address', 'Phone', 'Email', 'Age']
data = [
    {'Name': 'Sean', 'Address': '123, Oak Street, Taipei', 'Phone': '02-9876-5432', 'Email': "sean@gmail.com",
     'Age': 40},
    {"Name": "Amy", 'Address': "456, Park Avenue, Taichung", 'Phone': "04-8877-6655", 'Email': "amy@gmail.com",
     'Age': 30},
    {"Name": "David", 'Address': "789 First Road Tainan", 'Phone': "06-654-3210", 'Email': "david@gmail.com", 'Age': 25}
]

f = open("exFiles/contact3.csv", "w")
csvWriter = csv.DictWriter(f, header, dialect='unix')
csvWriter.writeheader()

for d in data:
    csvWriter.writerow(d)

f.close()
print("Data has output in to contact3.csv")

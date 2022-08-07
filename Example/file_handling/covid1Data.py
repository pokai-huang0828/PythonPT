import csv

f = open("exFiles/covid19_global_cases_and_deaths.csv", 'r', encoding='utf-8')

csvCursor = csv.DictReader(f)

print(f'{"國家":>10} |{"Country":>18} |{"Cases":>15} |{"Deaths":>12}')
count = 0
for row in csvCursor:
    if count < 20:
        print(f'{row["country_ch"]:>10} |{row["country_en"]:>18} |{row["cases"]:>15} |{row["deaths"]:>12}')
        count += 1

f.close()

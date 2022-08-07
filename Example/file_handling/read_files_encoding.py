# 檔案讀取 / 存取
import locale
import io
print("CP950")
f = open("Poem.txt", encoding='cp950')
line = f.readline()

while line:
    print(line, end='')
    line = f.readline()

print("UTF-8")
f2 = open("PoemUTF8.txt", encoding='utf-8')
line = f2.readline()

while line:
    print(line, end='')
    line = f2.readline()

# print(f.read())  # Read all lines
# print(f.read(6))  # Read first 6 words

# print(f.readline())  # Read first line
# print(f.readline())  # If continue to add f.readline, it will read next line

# print(f.readlines())  # Turn text in to list

# for x in f:  # Loop through the file line by line
#     print(x)

f.close()  # Close the file
f2.close()

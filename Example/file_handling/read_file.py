# 檔案讀取
filename = input("Please give your file name: ")

fin = open(filename)
line = fin.readline()

while line:
    print(line, end='')
    line = fin.readline()

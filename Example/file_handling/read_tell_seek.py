f = open("song.txt", "r")
str = f.read(15)
print("讀取的字串是 : ", str)

position = f.tell()
print("目前位置 : ", position)

position = f.seek(28, 0)
str = f.read(16)
print("重新調整後讀取的字串是 : ", str)

position = f.tell()
print("目前位置 : ", position)
f.close()

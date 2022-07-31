import sys

# print("匯入模組資訊: ", sys.modules)

# print("模組搜尋路徑: ", sys.path)

# print("命令列參數: ", sys.argv)

help(print)

sys.stdout.write("標準輸出: Hello World!\n")
# sys.stderr.write("錯誤輸出: Hello World!\n")

sys.stdout.write("請輸入姓名:")
name = sys.stdin.readline()
print("Hello", name)
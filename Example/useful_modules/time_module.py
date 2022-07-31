import time
print("三秒延遲開始!")
time.sleep(3)  # 延遲3秒鐘
print("三秒延遲完成!")

print(time.time())
time.sleep(2)
print(time.ctime())
time.sleep(2)
lt = time.localtime()

# Add '.' can select the value that you need
print(lt)
print(f"西元 {lt.tm_year}, {lt.tm_mon}月 {lt.tm_mday}日")

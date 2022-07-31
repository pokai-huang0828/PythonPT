from datetime import date

#  datetime 模組，內含date / time / datetime / timedelta 類別
#  date 類別代表日期相關的內容
#    date(year, month, day)：建立指定日期物件
#    date.today()：傳回目前系統日期時間物件
#    date.strftime(format)：設定系統日期顯示字串
#        %y：年(2位), %Y：年(4位), %m：月(數字), %b：月(文字), %d：日, %w：星期
#    date.isoformat() / str(date) 取得日期isoformat格式 yyyy-mm-dd
#    date.isoweekday() 取得1(星期一)~7(星期日)
#  time類別代表時間相關的內容
#    time(hour,minute,second,millisecond) ：建立指定時間物件
#    time()：建立00:00:00時間物件
#    time.strftime(format)：設定系統時間顯示字串
#  datetime類別代表日期加時間的內容
#    datetime(year, month, day, hour, minute, second, millisecond)：建立指定日期加時間物件
#  timedelta類別代表時間差
#    date相減會變成timedelta
#    以days為計算單位


now = date.today()
print(f"現在時間: {now}")

# 設定顯示格式        06-09-21. 09 Jun 2021.
print(now.strftime('%m-%d-%y. %d %b %Y.'))

birthday = date(1992, 8, 28)

age = now - birthday

print(age.days)

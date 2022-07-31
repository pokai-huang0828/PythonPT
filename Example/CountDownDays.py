from datetime import date


def daysBetween(date1, date2):
    diff = date1 - date2
    return diff.days


today = date.today()
while True:
    event = input('輸入事件(輸入q離開):')
    if event == 'q':
        print('程式結束')
        break
    dateStrs = input('輸入日期(yyyy-mm-dd):').split('-')
    eventDay = date(int(dateStrs[0]), int(dateStrs[1]), int(dateStrs[2]))
    if eventDay > today:
        print("距離%s還有%d天" % (event, daysBetween(eventDay, today)))
    else:
        print("%s已經過了%d天" % (event, daysBetween(today, eventDay)))

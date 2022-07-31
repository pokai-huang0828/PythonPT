from datetime import date


def calDays(startDate, targetDate):
    left = targetDate - startDate
    return left.days


while True:
    event = input("請輸入計算的事件(輸入 'exit' 離開): ")
    if event == "exit" or event == "Exit" or event == "EXIT":
        print("Good Bye~! :) 👋👋👋")
        break

    eveDate = input("請輸入事件目標日期(yyyy-mm-dd): ").split("-")
    eventDate = date(int(eveDate[0]), int(eveDate[1]), int(eveDate[2]))

    checkPoint = input("事件開始日期為今日嗎? (Y/N) ")
    if checkPoint == "Y" or checkPoint == "y":
        startDate = date.today()
    else:
        strDate = input("請輸入事件開始日期(yyyy-mm-dd): ").split("-")
        startDate = date(int(strDate[0]), int(strDate[1]), int(strDate[2]))

    if startDate < eventDate:
        result = calDays(startDate, eventDate)
        print(f"距離\"{event}\" 西元{eveDate[0]}年, {eveDate[1]}月{eveDate[2]}日還有 {result} 天!!\n")

    elif startDate == eventDate:
        print(f"今天就是 {event} !!")

    else:
        result = calDays(eventDate, startDate)
        print(f"距離西元{eveDate[0]}年, {eveDate[1]}月{eveDate[2]}日的\"{event}\"已經過了 {result} 天!!\n")


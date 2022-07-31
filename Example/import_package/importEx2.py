import temperature2 as temp

tf = float(input("請輸入華氏溫度: "))
tc = temp.F2C(tf)

print("華氏 %.0f 度等於攝氏 %.0f 度" % (tf, tc))

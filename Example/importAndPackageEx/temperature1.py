# 匯入套件
#  import 套件.模組
#  import 套件.模組 as 別名名稱
#  from 套件 import 模組
#  from 套件.模組 import 函式或變數
#  使用套件
#  套件.模組.函式或變數
#  別名名稱.函式或變數
#  模組.函式或變數
#  函式或變數

import sys
# print(sys.path)
# print(sys.modules)

def C2F(tempC):
    return 9 / 5 * tempC + 32

def F2C(tempF):
    return (tempF - 32) / 9 * 5


print("__name__", __name__, end="\n\n")

tc = float(input("請輸入攝氏溫度: "))
tf = C2F(tc)
print("攝氏 %.0f 度等於華氏 %.0f 度" % (tc, tf))

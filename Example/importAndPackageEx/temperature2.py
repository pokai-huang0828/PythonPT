def C2F(tempC):
    return 9 / 5 * tempC + 32

def F2C(tempF):
    return (tempF - 32) / 9 * 5


print("__name__", __name__, end="\n\n")


def main():
    tc = float(input("請輸入攝氏溫度: "))
    tf = C2F(tc)
    print("攝氏 %.0f 度等於華氏 %.0f 度" % (tc, tf))

if __name__=='__main__':
    main()


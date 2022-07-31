import random

lottoNums = random.sample(range(1, 50), 6)

specialNum = 0
while not specialNum and specialNum in lottoNums:
    specialNum = random.randint(1,49)

print('樂透號碼:', sorted(lottoNums))
print('特別號:', specialNum)

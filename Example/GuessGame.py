import random

start, end = 1, 100
answer = random.randint(start, end)
guess = int(input('猜一個%d~%d的整數:' % (start, end)))
count = 1

while count < 5:
    if guess == answer:
        print('猜對了!')
        break
    elif guess > answer:
        end = guess - 1
    else:
        start = guess + 1
    count += 1
    guess = int(input('猜一個%d~%d的整數:' % (start, end)))
else:
    print("答案是:%d" % answer)

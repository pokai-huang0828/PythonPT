import random

start, end = 1, 100
answer = random.randint(start, end)
print(answer)
guess = int(input(f"Guess a number between {start} ~ {end}: "))
count = 5

while count > 0:
    if guess < start or guess > end:
        print("\n **Wrong input! Your number can't over range... Try again!!**\n")
    if guess == answer:
        print(f"You got it!! The answer is {answer}!")
        break
    elif guess > answer:
        end = guess - 1
    elif guess < answer:
        start = guess + 1
    count -= 1
    print(f"Wrong one... You still have {count} times!")
    guess = int(input(f"Guess a number between {start} ~ {end}: "))
else:
    print(f"You have no chance... the answer is {answer}.")

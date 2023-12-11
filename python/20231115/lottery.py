import random

lottery = sorted(random.sample(range(1, 49), 6))

guessLottery = []
for i in range(6):
    guess = int(input("請輸入一個數字(1~49): "))
    guessLottery.append(guess)

lotteryPrice = 10
for guess in guessLottery:
    if guess in lottery:
        lotteryPrice *= 10

print("Lottery prize:", lotteryPrice)

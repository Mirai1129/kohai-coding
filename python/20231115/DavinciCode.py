import random

lowest = 0
highest = 100
answer = random.randint(0, 100)

while True:
    try:
        guessNumber = int(input(f"請輸入{lowest}~{highest}之間的數字: "))
        if guessNumber == answer:
            print("答對了！")
            break
        else:
            if guessNumber < lowest or guessNumber > highest:
                print(f"請輸入{lowest}~{highest}之間的數字！")
            elif guessNumber < answer:
                lowest = guessNumber
                print(f"範圍在{lowest}~{highest}")
            else:  # if guessNumber > answer:
                highest = guessNumber
                print(f"範圍在{lowest}~{highest}")
    except ValueError:
        print("請輸入有效的數字！")

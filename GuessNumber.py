import random

guess=random.randint(0,100)
cnt=0

while True:
    num=int(input("Enter number between 0 to 100 :"))
    cnt+=1

    if num==guess:
        print("You are win right num are:",num)
        print("Attempts:", cnt)
        break
    elif num>guess:
        print("Your guessing number is too high")
        continue
    elif num<guess:
        print("Your guessing number is too low")
        continue

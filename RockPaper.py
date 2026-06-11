import random

while True:

    Ak = input("Enter your choice (paper, rock, scissors): ")

    List = ['paper', 'rock', 'scissors']
    Me = random.choice(List)

    print("Computer chose:", Me)

    if Ak == Me:
        print("Draw! Play again.")
        continue

    elif (Ak == 'paper' and Me == 'rock') or \
         (Ak == 'rock' and Me == 'scissors') or \
         (Ak == 'scissors' and Me == 'paper'):

        print("Shivam Win")
        break

    else:
        print("Computer Wins")
        break
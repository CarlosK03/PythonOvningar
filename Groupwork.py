import random
import time

print("ROCK, PAPER, SCISSORS")


Moves=["r","p","s"]
# It's a while loop that assigns the input to Move1 and then checks if it's not equal to q.
while (Move1 :=input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ").lower()) != "q":
    if Move1 in {"r", "p", "s"}:
        Move2 = random.choice(Moves)
        if Move1=="r":
            print("You chose ROCK")
            if Move2=="s":
                print("AI chose scissors. You win!")
            elif Move2=="p":
                print("AI chose paper, you lose")
            elif Move2=="r":
                print("AI chose rock too. It's a tie!")
        elif Move1=="p":
            print("You chose PAPER")
            if Move2=="s":
                print("AI chose scissors. You lost!")
            elif Move2=="p":
                print("AI chose Paper, you went even!")
            elif Move2=="r":
                print("AI chose rock, you've won!")
        elif Move1=="s":
            print("You chose SCISSORS")
            if Move2=="s":
                print("AI chose Scissors, you went even!")
            elif Move2=="p":
                print("AI chose Paper, you've won!")
            elif Move2=="r":
                print("AI chose Rock, you lost!")

exit()


rock = 1
paper = 2
scissor = 3

import random


print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

while True:
    print("reem pick \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
    reem_pick = int(input("reem picked: "))
    while reem_pick < 1 or reem_pick > 3 :
        pick = int(input("you cannot pick this number!: "))
    if reem_pick == 1:
        reem_picked = 'rock'
    if reem_pick == 2:
        reem_picked = 'paper'
    if reem_pick == 3:
        reem_picked = 'scissor'
    print("reem picked: " + reem_picked)
    print("\nTime for computer to pick...")
    computer_pick = random.randint(1, 3)
    computer_pick == pick:
        computer_pick = random.randint(1, 3)
        if computer_pick == 1:
            computer_picked = 'rock'
        if computer_pick == 2:
            computer_picked = 'paper'
        if computer_pick == 3:
            computer_picked = 'scissor'

    print("Computer pick is: " + computer_picked)
    print(reem_picked + " V/s " + computer_picked)

    if reem_pick == computer_pick:
        print("Draw")
        result = Draw

        if ((reem_pick == 1 and computer_pick == 2) or
                (reem_pick == 2 and computer_pick == 1)):
            print("paper wins => ")
            result = "paper"

        if ((reem_pick == 1 and computer_pick == 3) or
              (reem_pick == 3 and computer_pick == 1)):
            print("Rock wins =>")
            result = "Rock"

        else:
            print("scissor wins =>")
            result = "scissor"


    if result == Draw:
        print("<==  draw ==>")
    if result == reem_pick:
        print("<== reem wins ==>")
    if result == computer_pick:
        print("<== Computer wins ==>")


        print("one more game? (Y/N)")
        ans = input()

        if ans == 'n':


print("\nhave a nice day")





    pass

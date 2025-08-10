# Rock wins againts Scissor
# Scisor wins against Paper
# paper Wins against 

import random

User_Choice = int(input("Enter your choice (0: Rock, 1: Paper, 2: Scissors): "))

if User_Choice < 0 or User_Choice > 2:
    print("You entered an invalid number. You lose!")
else:
    Computer_Choice = random.randint(0, 2)
    print("Computer's choice:", Computer_Choice)

    if Computer_Choice == User_Choice:
        print("It's a draw!")
    elif (User_Choice - Computer_Choice) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")

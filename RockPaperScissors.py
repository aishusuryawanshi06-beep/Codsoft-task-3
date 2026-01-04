# Rock Paper Scissors Program

import random

user_score = 0
computer_score = 0

win_rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
while True:
    user = input("\nEnter rock, paper or scissors:").lower()
    
    if user not in win_rules:
        print("Invalid input! Try again")
        continue
    computer = random.choice(list(win_rules.keys()))
    
    print("You choose:", user)
    print("Computer choose:", computer)
    
    if user == computer:
        print("It's a tie!🤝")
    elif win_rules[user] == computer:
        print("You Win!🥳")
        user_score += 1
    else:
        print("You Lose!😢")
        computer_score += 1
        
    print("Your score:", user_score)
    print("Computer score:", computer_score)
    
    again = input("\nPlay again? (yes/no):").lower()
    if again != "yes":
        print("Game over!")
        print("Thank You for Playing!😊")
        break
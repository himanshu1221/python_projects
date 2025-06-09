import random

user_wins = 0
computer_wins = 0
ties = 0

while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    else:
        random_number = random.randint(0, 2)
        computer_input = ["rock", "paper", "scissors"][random_number]
        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid input, please try again.")
            continue
        if user_input in ["rock", "paper", "scissors"]:
            print(f"Computer chose: {computer_input}")
            if user_input == computer_input:
                print("It's a tie!")
                ties += 1
            elif (user_input == "rock" and computer_input == "scissors") or \
                 (user_input == "paper" and computer_input == "rock") or \
                 (user_input == "scissors" and computer_input == "paper"):
                print("You win!")
                user_wins += 1
            else:
                print("You lose!")
                computer_wins += 1
            print("score: you: {}, computer: {}, ties: {}".format(user_wins, computer_wins, ties))
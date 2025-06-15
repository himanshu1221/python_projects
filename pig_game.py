import random

score = 0 # Initialize score

def random_roll():
    rand_num = random.randint(1, 6) # Generate a random number between 1 and 6
    return rand_num

value = random_roll()

while True:
    players = input("How many players are playing? (2-4): ")
    if players.isdigit():
        players = int(players)
        if players < 2 or players > 4:
            players = input("Invalid input. Please enter a number between 2 and 4: ")
        if players >= 2 and players <= 4:
            print(f"Starting the game with {players} players.")
            break
    else:
        print("Invalid input. Please enter a number.")

max_score = 50
player_scores = [0 for _ in range(players)]  # Initialize player scores
#print(player_scores)

while max(player_scores) < max_score: # Continue until a player reaches the max score
    
    current_score = 0
    
    should_roll = input("Do you want to roll the dice? (yes/no): ").lower()
    if should_roll == "no":
        break
    if should_roll == "yes":
        value = random_roll()
        if value == 1:
            print("You rolled a 1!")
            break
    else:
        current_score += value
        print(f"You rolled a {value}.")

    print("Your current score is:", current_score)
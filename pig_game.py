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

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn")
        current_score = 0 # Initialize current score for the player
        
        while True: # Loop until the player decides to roll or rolls a 1
            should_roll = input("Do you want to roll the dice? (yes/no): ").lower() # Ask if the player wants to roll the dice
            if should_roll != "yes": # Player chooses to roll the dice
                break
            value = random_roll() # Roll the dice
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0 # Reset current score if a 1 is rolled
                break
            else:
                current_score += value
                print(f"You rolled a {value}")

            print(f"Current score: {current_score}")
        
        player_scores[player_idx] += current_score # Add the current score to the player's total score

        print("your total score is now:", player_scores[player_idx])
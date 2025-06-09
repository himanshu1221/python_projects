import random

print("Random number guesser")

max_range = input("enter the range: ")
if max_range.isdigit():
    max_range = int(max_range)
    print("guess a number between 0 and "+ str(max_range))
else:
    print("Invalid input please enter a number")
    exit()

random_number = random.randint(0,max_range)

guesses = 0

while True:
    guesses += 1
    guess = input("guess the number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid input please enter a number")
        continue
    if guess == random_number:
        print("You guessed it right!")
        break
    elif guess < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    
print("You guessed the number in " + str(guesses) + " guesses")
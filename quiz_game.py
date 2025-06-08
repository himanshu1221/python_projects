print("Quiz Game begins!")

concent = input("Do you want to play the quiz game? (yes/no): ").lower() #LOWER IS USED TO MAKE THE INPUT CASE INSENSITIVE

if concent == "yes":
    print("Great! lets begin!")

    score = 0  # Initialize score

    question = input("Full form of RAM: ").lower()  # LOWER IS USED TO MAKE THE INPUT CASE INSENSITIVE
    if question == "random access memory":
        score += 1  # Increment score if the answer is correct
        print("Correct!")
    else:
        score += 0  # No increment if the answer is incorrect
        print("Incorrect!")
    


    question = input("Full form of CPU: ").lower()  # LOWER IS USED TO MAKE THE INPUT CASE INSENSITIVE
    if question == "central processing unit":
        score += 1  # Increment score if the answer is correct
        print("Correct!")
    else:
        score += 0  # No increment if the answer is incorrect
        print("Incorrect!")


    question = input("Full form of GPU: ").lower()  # LOWER IS USED TO MAKE THE INPUT CASE INSENSITIVE
    if question == "graphics processing unit":
        score += 1  # Increment score if the answer is correct
        print("Correct!")
    else:
        score += 0  # No increment if the answer is incorrect
        print("Incorrect!")


    
    question = input("Full form of MAP: ").lower()  # LOWER IS USED TO MAKE THE INPUT CASE INSENSITIVE
    if question == "memory access protocol":
        print("Correct!")
        score += 1  # Increment score if the answer is correct
    else:
        score += 0  # No increment if the answer is incorrect
        print("Incorrect!")

    print(f"Your score is: {score} out of 4")  # Display the final score

else:
    print("Ok, maybe next time!")
    quit()
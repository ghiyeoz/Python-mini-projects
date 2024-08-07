import random  # Import the random module for generating random numbers

top_of_range = input("Type a number: ")  # Ask the user to type a number and store it in the variable 'top_of_range'

if top_of_range.isdigit():  # Check if the input is a digit
    top_of_range = int(top_of_range)  # Convert the input to an integer

    if top_of_range <= 0:  # Check if the number is less than or equal to 0
        print("Please type a number larger than 0 next time.")  # Inform the user to enter a number larger than 0
        quit()  # Exit the program
else:
    print('Please type a number next time.')  # Inform the user to enter a valid number
    quit()  # Exit the program

random_number = random.randint(0, top_of_range)  # Generate a random number between 0 and the user-provided number
while True:  # Start an infinite loop
    user_guess = input("Make a guess:")  # Ask the user to make a guess and store it in 'user_guess'
    if user_guess.isdigit():  # Check if the guess is a digit
        user_guess = int(user_guess)  # Convert the guess to an integer
    else:
        print("Please type a number next time")  # Inform the user to enter a valid number
        continue  # Continue to the next iteration of the loop
    
    if user_guess == random_number:  # Check if the user's guess matches the random number
        print("You got it!")  # Inform the user that they guessed correctly
        break  # Exit the loop

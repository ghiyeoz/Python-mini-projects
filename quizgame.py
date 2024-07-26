print("Welcome to my computer quiz!")
# Prints "Welcome to my computer quiz!" to the screen.

playing = input("Do you want to play? ")
# Asks the user "Do you want to play?" and stores the answer in the variable 'playing'.

if playing.lower() != "yes":
    quit()
# If the user's answer is not 'yes', the program exits.

print("Okay! Let's play :)")
# If the user answered 'yes', prints "Okay! Let's play :)" to the screen.

score = 0
# Initializes the variable 'score' to 0, which will count the number of correct answers.

answer = input("What does CPU stand for? ")
# Asks the user "What does CPU stand for?" and stores the answer in the variable 'answer'.

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
# If the user's answer is "central processing unit", prints "Correct!" and increments 'score' by 1.
else:
    print("Incorrect!")
# If the answer is incorrect, prints "Incorrect!".

answer = input("What does GPU stand for? ")
# Asks the user "What does GPU stand for?" and stores the answer in the variable 'answer'.

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
# If the user's answer is "graphics processing unit", prints "Correct!" and increments 'score' by 1.
else:
    print("Incorrect!")
# If the answer is incorrect, prints "Incorrect!".

answer = input("What does RAM stand for? ")
# Asks the user "What does RAM stand for?" and stores the answer in the variable 'answer'.

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
# If the user's answer is "random access memory", prints "Correct!" and increments 'score' by 1.
else:
    print("Incorrect!")
# If the answer is incorrect, prints "Incorrect!".

answer = input("What does PCU stand for? ")
# Asks the user "What does PCU stand for?" and stores the answer in the variable 'answer'.

if answer.lower() == "power control unit" or answer.lower() == "power conversion unit":
    print("Correct!")
    score += 1
# If the user's answer is "power control unit" or "power conversion unit", prints "Correct!" and increments 'score' by 1.
else:
    print("Incorrect!")
# If the answer is incorrect, prints "Incorrect!".

print("You got " + str(score) + " questions correct!")
# Prints the number of questions the user got correct, e.g., "You got 3 questions correct!".

print("You got " + str((score / 4) * 100) + "%.")
# Prints the user's score as a percentage, e.g., "You got 75.0%."
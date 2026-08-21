import random
import sys

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        sys.exit()
else:
    print("Please type a number next time.")
    sys.exit()

number = random.randint(1, top_of_range)

guesses = 0
while True:
    guesses += 1
    number = random.randint(1, top_of_range)
    user_guess = input("Make a guess of the number between 1 and " + str(top_of_range) + ": ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == number:
        print("You got it!")
        break
    else:
        if user_guess > number:
            print(f"You were above the number! Guess number is {number}")
        else:
            print(f"You were below the number! Guess number is {number}")

print(f"You got it in {guesses} guesses!")
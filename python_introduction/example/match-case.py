import random

age = int(input("Enter your age: "))

def has_id(user):
   return user =='yes'


match age:
    case 18 | 19:  # Match multiple values with pipe (|)
        if age >= 18 and has_id():  # Guard using a function call
            print("You are eligible to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("You are not yet eligible to vote.")



secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
counter  = 0






# If the guess is correct, display a message like “Congratulations, you guessed it!”
# If the guess is too high, display a message like “Oops, your guess is a bit high. Try again!”
# If the guess is too low, display a message like “Nope, your guess is a bit low. Give it another shot!”
# Offer to play again: Ask the user if they want to play again using an if statement and user input.
# Exercise 2: Math Quiz with Exception Handling
# This program generates two random numbers and asks the user to add them.
# It also handles invalid input using try and except.


# Import the standard library module for random numbers
import random

# Generate two random integers between 1 and 10
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Ask the user the math question
print(f"What is {num1} + {num2}?")
answere = input("Your answere:")

try:
    # Try to convert the user's input into an integer
    user_answere = int(answere)

     # Calculate the correct answer
    correct_answere = num1 + num2
    
    
    # Check if the user's answer is correct
    if user_answere == correct_answere:
       print("Correct!!")

    else:
        print(f"Sorry, that is wrong! The correct answere is {correct_answere}")

except ValueError:
    # This runs if the user enters something that cannot be converted to a number
    print("Invalid input!")



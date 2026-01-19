# ============================================
# Exercise 1: File to List Converter
# ============================================
# This script reads content from a text file and converts each line
# into an element in a Python list.
# The goal is to practice basic file handling and error handling.

# Ask the user for the filename
filename = input("Filename: ")

try:
    # Open the file in read mode ("r")
    # This creates a file object we can work with
    file = open(filename, "r")

    # Read the entire file as one string and split it into lines
    # splitlines() removes the line breaks (\n) automatically
    lines = file.read().splitlines()

    # Close the file after reading
    # This is important to free system resources
    file.close()

    # Create an empty list to store the cleaned lines
    cleaned_lines = []

    # Loop through each line from the file
    for line in lines:
    # Convert the first letter of each word to uppercase
    # and add the formatted string to the list
        cleaned_lines.append(line.title())


    # Print the final list
    print(cleaned_lines)

except FileNotFoundError:
    # This runs if the file does not exist
    # Instead of crashing, the program prints a friendly error message
    print("Error: File not found. Check the filename and try again.")

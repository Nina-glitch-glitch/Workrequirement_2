# Exercise 1: File to List Converter

filename = input("Filename: ")


try:
    with open(filename, "r") as file:

        lines = file.readlines()  # list of lines (strings)

    # Remove whitespace (newline, spaces) from each line
    cleaned_lines = [line.strip() for line in lines]

    print(cleaned_lines)

except FileNotFoundError:
    print("Error: File not found. Check the filename and try again.")

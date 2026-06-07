"""
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
try:
    file = open("sample.txt", "r")
    print("Reading file content:\n")
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
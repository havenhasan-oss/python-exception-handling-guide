# This example demonstrates common exceptions that may occur in Python.

number = [1, 2]

# Accessing an index that does not exist in the list will raise an IndexError
# print(number[3])  # IndexError: list index out of range

# Converting user input to an integer.
# If the user enters a non-numeric value, Python will raise a ValueError.
age = int(input("Age: "))
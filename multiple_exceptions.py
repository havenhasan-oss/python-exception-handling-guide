# This example demonstrates how to handle multiple exceptions.

try:
    age = int(input("Age: "))

    # This may raise a ZeroDivisionError if age equals 0
    xfactor = 10 / age

# Handle both ValueError and ZeroDivisionError in one block
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")

# Executes if no exception occurs
else:
    print("No exception was thrown.")
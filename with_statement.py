# This example demonstrates using the 'with' statement for automatic resource management.

try:
    # The 'with' statement automatically closes the file after use
    with open("main.py") as file:
        print("File opened.")

    age = int(input("Age: "))
    xfactor = 10 / age

# Handle invalid input or division by zero
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")

# Executes if no exception occurs
else:
    print("No exception was thrown.")
# This example demonstrates how to raise a custom exception.

def calculate_xfactor(age):

    # Validate the input value
    # If age is zero or negative, raise a ValueError
    if age <= 0:
        raise ValueError("Age can't be 0 or less.")

    # Return the calculated value
    return 10 / age


age = int(input("Age: "))

try:
    # Call the function and print the result
    print(calculate_xfactor(age))

# Handle the raised ValueError
except ValueError as error:
    print(error)
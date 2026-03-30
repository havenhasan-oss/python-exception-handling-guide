# This example demonstrates how to handle exceptions using try and except blocks.

try:
    # Attempt to convert the user input into an integer
    age = int(input("Age: "))

# If the input is not a valid integer, a ValueError will be raised
except ValueError as ex:
    print("You didn't enter a valid age.")
    
    # Print the error message
    print(ex)
    
    # Print the type of the exception
    print(type(ex))

# This block executes only if no exceptions occur
else:
    print("No exceptions were thrown.")

# This line always executes
print("Execution continues.")
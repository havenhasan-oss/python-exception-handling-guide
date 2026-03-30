# This example demonstrates resource cleanup using the finally block.

try:
    # Open a file (this allocates a system resource)
    file = open("main.py")

    age = int(input("Age: "))
    xfactor = 10 / age

# Handle possible input or division errors
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")

# Executes if the try block completes successfully
else:
    print("No exception was thrown.")

# The finally block always executes
# It is commonly used to release resources like files or database connections
finally:
    file.close()
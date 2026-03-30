# This example compares the performance cost of raising exceptions
# versus using conditional validation.

from timeit import timeit

# Code example that raises an exception
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be 0 or less.")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

# Code example that avoids raising exceptions
# and instead uses conditional checks
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)

if xfactor == None:
    pass
"""

# Measure execution time for both approaches
print("First code =", timeit(code1, number=10000))
print("Second code =", timeit(code2, number=10000))
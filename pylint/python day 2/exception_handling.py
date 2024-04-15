"""
Exception Handling Assignments
"""

# Write a Python program that takes two integers as input and performs division (num1 / num2).
# Handle the ZeroDivisionError and display a custom error message when the second number is zero.

import logging

logging.basicConfig(
    filename="exception_handling.log", encoding="utf-8", level=logging.DEBUG
)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    logging.error("%s", e)


# Write a Python program that takes user input for age.
# Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120.
class InvalidAgeError(Exception):
    """custom exception class for invalid age input"""


try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    print(age)
except InvalidAgeError as e:
    logging.error("%s", e)

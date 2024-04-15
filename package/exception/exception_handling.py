# Write a Python program that takes two integers as input and performs division (num1 / num2). Handle the ZeroDivisionError and display a custom error message when the second number is zero.
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
    logging.error(e)


# Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. Handle the FileNotFoundError and display an error message if the file is not found.

try:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        contents = file.read()
        print("File Content: ")
        print(contents)

except FileNotFoundError as e:
    logging.error(e)

# Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error message when the input cannot be converted to an integer.

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as e:
    logging.error(e)


# Write a Python program that takes two integers as input and performs division (num1 / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)
except ValueError as e:
    logging.error(e)
except ZeroDivisionError as e:
    logging.error(e)

# Write a Python program that takes user input for age. Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120.


class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    print(age)
except InvalidAgeError as e:
    logging.error(f"{e}")


# Implement a program that reads user input for a password. Create a custom exception WeakPasswordError to handle cases where the password is shorter than 8 characters.


# Hint: WeakPasswordError that inherits Exception class
class WeakPasswordError(Exception):
    pass


try:
    password = input("Enter new password: ")
    if len(password) < 8:
        raise WeakPasswordError("Password length should be greater than 8")
except WeakPasswordError as e:
    logging.error(f"{e}")

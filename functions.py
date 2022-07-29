import math

## opens a file in read mode
## filename received as a parameter
# CORRECTIONS:
# added custom exceptions for empty string and not string
# try/except/else for empty string, file not found, not string
class NotStringError(Exception):
    pass
class EmptyStringError(Exception):
    pass
def openFile(filename):
    try:
        if not filename:
            raise EmptyStringError
        if not isinstance(filename, str):
            raise NotStringError
        infile = open(filename, "r")
    except FileNotFoundError:
        print("File not found.")
    except EmptyStringError:
        print("Empty string.")
    except NotStringError:
        print("Not string.")
    else:
        print("File opened.")

## takes two numbers and returns
## the result of a division
# CORRECTIONS:
# try/except/else for divide by zero, type error
# added round (to base 1) function
def numbers(num1, num2):
    try:
        result = round(num1 / num2, 1)
    except TypeError:
        return "Not integer."
    except ZeroDivisionError:
        return "Cannot divide by zero."
    else:
        return result

## takes in two points
## finds the distance between the points
# CORRECTIONS:
# try/except/else for 
# added absolute and round (to base 1) functions
def dist(x1, y1, x2, y2):
    try:
        dist = abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2
        dist = round(math.sqrt(dist), 1)
    except TypeError:
        return "Not integer."
    else:
        return dist

## takes in a string -- reverses it
## then compares the two
# CORRECTIONS:
# try/except/else
# catches if something isn't a palindrome
# catches if its not a string
def isPalindrome(temp):
    try:
        test = temp[::-1]
        if(test != temp):
            raise AssertionError
    except AssertionError:
        return "Not a palindrome."
    except TypeError:
        return "Not a string."
    else:
        return True

## has input to receive two numbers
## divides the two, then outputs the result
# CORRECTIONS:
# try/except/else
# No return values, so print only
# catches division errors & if not an int
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ValueError:
        print("Not an int.")
    else:
        print("Your numbers divided is:", div)

## returns the squareroot of a particular number
# CORRECTIONS:
# try/except/else
# catches if not an int
# catches if int is negative
# rounds to 1 decimal place
def sq(num):
    try:
        math.sqrt(num)
    except TypeError:
        return "Not an int."
    except ValueError:
        return "ERROR - Invalid Input"
    else:
        return round(math.sqrt(num), 1)

## grabs user's name
## greets them by their entire name
## names should be strings
# CORRECTIONS:
# none failed, but paramater was names only, no numbers
# if/else
# Needed string only parameters
# all vars tested for if string
def greetUser(first, middle, last):
    if(type(first) == str and type(middle) == str and type(last) == str):
        print("Hello!")
        print("Welcome to the program", first, middle, last)
        print("Glad to have you!")
    else:
        print("Not a string.")

## takes in a Python list
## attempts to display the item at the index provided
# CORRECTIONS:
# try/except
# tests if in range of list (pos or neg)
# tests if int
def displayItem(numbers, index):
    try:
            print("Your item at", index, "index is", numbers[index])
    except IndexError:
        print("ERROR - Index out of range.")
    except ValueError:
        print("Not an integer.")
    except TypeError:
        print("Not an integer.")

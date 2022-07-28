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
def isPalindrome(temp):
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])

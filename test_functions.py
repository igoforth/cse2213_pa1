from pickle import NONE
import pytest
from functions import *

# openFile
# test 1: Will succeed with testing.txt
# test 2: Tests for share.txt (Cannot find)
# test 3: Tests for empty string
# test 4: Tests for integer input
@pytest.mark.parametrize("file,message",
                        [("testing.txt", "File opened."),
                        ("share.txt", "File not found."),
                        ("", "Empty string."),
                        (42, "Not string.")])
def test_openFile(capsys, file, message):
    openFile(file)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == message

# numbers
# testing division with int and floats
# passes first 2
# 3rd fails due to decimal rounding
# 4th fails due to TypeError -> cannot be a string
# 5th passes -> ZeroDivisionError -> cannot divide by zero
# 6th passes bc -> False == 0
@pytest.mark.parametrize("num1,num2,div",
                        [(4, 2, 2),
                        (8.6, 4.3, 2),
                        (45, 23, 1.9),
                        ('6', '3', '2'),
                        (7, 0, "Cannot divide by zero."),
                        (False, 7, 0)])
def test_numbers(num1, num2, div):
    assert numbers(num1, num2) == div


# dist
# dist is neg? -> cant be neg due to squaring
# round to how many decimals?
# first passes 
# second passes
# third fails for type error
@pytest.mark.parametrize("x1,y1,x2,y2,distance",
                        [(1, 2, 3, 4, 2.8),
                        (0, 0, 0, 0, 0),
                        ('1', '4', '5', '5', '4.1')])
def test_dist(x1, y1, x2, y2, distance):
    assert dist(x1, y1, x2, y2) == distance


# isPalindrome
# first 3 pass, 'clear' fails but isn't handled when not a palindrome
# False fails and isn't handled with TypeError -> bool
# 66 is a palindrome but fails because of TypeError -> integer
@pytest.mark.parametrize("palin, result" ,
                        [('racecar', True),
                         ('55', True),
                         ('stats', True), 
                         ('clear', True ),
                         (False, True), 
                         (66, True)])
def test_isPalindrome(palin, result):
    assert isPalindrome(temp) == result

# helper function for test_divide
def geninputs(num1, num2):
    inputs = [num1, num2]

    for item in inputs:
        yield item

# divide
# test 1: 4 / 2 = 2 succeed
# test 2: 1 / 0 = ? would succeed because you can not divide by zero
# test 3: 'y' / '4' = ?  fail due to string input
@pytest.mark.parametrize("num1,num2, answer",
                        [(4,2,"Your numbers divided is: 2.0"),
                        (1,0,"You cannot divide by zero."),
                        ('y','4',"y/4")])
def test_divide(monkeypatch, num1, num2,answer):
    GEN = geninputs(num1, num2)
    monkeypatch.setattr("builtins.input", lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == answer
    

# sq
# first pass, second fail (returns a decimal of 3.2), third pass, 4th pass -> 'y' yields "Not an int", 5th pass -> -4 yields "ERROR - Invalid Input"
@pytest.mark.parametrize("num,out",
                        [(4, 2),
                        (10, "ERROR - Invalid Input"),
                        (144, 12),
                        ('y', "Not an int."),
                        (-4, "ERROR - Invalid Input")])
def test_sq(num, out):
    assert sq(num) == out


# greetUser
# all pass because all can identify as strings
# testing input and output
# test 1: normal strings succeed
# test 2: numbers succeed
# test 3: spaces in string input succeed
# test 4: empty strings succeed
# Supposed to only accept letters as names -> set limitation
@pytest.mark.parametrize("first,middle,last,expected",
                        [("Peter", "Benjamin", "Parker", "Hello!\nWelcome to the program Peter Benjamin Parker\nGlad to have you!"),
                        (1, 2, 3, "Hello!\nWelcome to the program 1 2 3\nGlad to have you!"),
                        ("Walter", "Pensky", "Jackson IV", "Hello!\nWelcome to the program Walter Pensky Jackson IV\nGlad to have you!"),
                        ('', '', 't', "Hello!\nWelcome to the program   t\nGlad to have you!")])
def test_greetUser(capsys, first, middle, last, expected):
    greetUser(first, middle, last)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

# displayItem
# first passes
# second fails -> IndexError -> out of range
# third fails -> IndexError -> should not have a negative index
# fourth fails -> TypeError -> cannot be a float
# fifth fails -> TypeError -> cannot be a string
@pytest.mark.parametrize("numbers,index,expected",
                        [([1, 5, 9, 8], 2, "Your item at 2 index is 9"),
                        ([5, 7, 6, 3, 1], 5, "Your item at 5 index is 0"),
                        ([9, 6, 2, 1, 99], -9, "Your item at -9 index is 0"),
                        ([8, 7, 2, 8], 2.5, "Your item at 2.5 index is 0"),
                        ([7, 4, 0, 1], '1', "Your item at 1 index is 4")])
def test_displayItem(capsys, numbers, index, expected):
    displayItem(numbers, index)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

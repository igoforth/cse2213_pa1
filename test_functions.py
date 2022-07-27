from pickle import NONE
import pytest 
from functions import * 

#openFile
# tests the file name, needs to have an if failed do this
def test_openFile(capsys):
    openFile('testing.txt')
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File opened."

#initially going to fail
#FNF error
#if failed -> say file not opened
def test_openFile(capsys):
    openFile('testing')
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File not opened."


#numbers
#testing division with int and floats
#passes first 2, fails 3rd bc it isn't equal -> create if doesn't equal
#4th fails due to decimal rounding
@pytest.mark.parametrize("num1,num2,div",[(4,2,2),(8.6,4.3,2),(42,7,7),(45,23,1.9)])
def test_numbers(num1, num2,div):
    assert numbers(num1,num2) == div


#dist
#dist is neg? -> cant be neg due to squaring
#round to how many decimals?
#first fails because of decimal rounding
#second passes
#third fails for type error
@pytest.mark.parametrize("x1,y1,x2,y2,distance",[(1,2,3,4,2.8),(0,0,0,0,0),('1','4','5','5',0)])
def test_dist(x1,y1,x2,y2,distance):
    assert dist(x1,y1,x2,y2) == distance


@pytest.mark.parametrize("temp",['racecar','55','stats','clear'])
def test_isPalindrome(temp):
    assert isPalindrome(temp)



#divide
def geninputs():
    inputs = ['6','3']

    for item in inputs:
        yield item

GEN = geninputs()
def test_divide(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    assert divide() == 2.0







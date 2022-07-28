from pickle import NONE
import pytest 
from functions import * 

#openFile
# tests the file name, needs to have an if failed do this
def test_openFile(capsys):
    openFile("testing.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File opened."

#initially going to fail
#FNF error
def test_openFile(capsys):
    openFile("share.txt")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File not found"

#FNF error
def test_openFile(capsys):
    openFile("")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File not found"

#OSError -> need an actual file name
def test_openFile(capsys):
    openFile(42)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "File not found"
    


#numbers
#testing division with int and floats
#passes first 2, fails 3rd bc it isn't equal -> create if doesn't equal
#fourth fails due to decimal rounding
#5th fails due to TypeError -> cannot be a string
#6th fails -> ZeroDivisionError -> cannot divide by zero
#7th passes bc -> False == 0
@pytest.mark.parametrize("num1,num2,div",[(4,2,2),(8.6,4.3,2),(42,7,7),(45,23,1.9),('6','3',2),(7,0,0),(False,7,0)])
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


#isPalindrome
#first 3 pass, 'clear' fails but isn't handled when not a palindrome
#False fails and isn't handled with TypeError -> bool
#66 is a palindrome but fails because of TypeError -> integer
@pytest.mark.parametrize("temp",['racecar','55','stats','clear',False,66])
def test_isPalindrome(temp):
    assert isPalindrome(temp)



#divide
#first passes, second fails because of the y
def geninputs():
    inputs = ['6','3']
    inputs_2 = ['y','2']

    for item in inputs:
        yield item
    
    for item_2 in inputs_2:
        yield item_2

GEN = geninputs()
def test_divide(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: next(GEN))

    assert divide() == None

#sq
#first pass, second fail (round to 1 decimal), third pass, 4th fail -> TypeError, 5th fail -> math domain error -> cannot sqroot a neg number
@pytest.mark.parametrize("num,out",[(4,2),(10,3.2),(144,12),('y',7),(-4,2)])
def test_sq(num,out):
    assert sq(num) == out




#greetUser 
#all pass because all can identify as strings
#testing input and output
@pytest.mark.parametrize("first,middle,last,expected",[("Peter", "Benjamin", "Parker","Hello!\nWelcome to the program Peter Benjamin Parker\nGlad to have you!"),(1,2,3,"Hello!\nWelcome to the program 1 2 3\nGlad to have you!"), ("Walter", "Pensky", "Jackson IV","Hello!\nWelcome to the program Walter Pensky Jackson IV\nGlad to have you!")])
def test_greetUser(capsys,first,middle,last,expected):
    greetUser(first,middle,last)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

#does not crash, but need to set parameters for being empty
@pytest.mark.parametrize("first,middle,last,expected",[('','','t',"Hello!\nWelcome to the program   t\nGlad to have you!")])
def test_greetUser2(capsys,first,middle,last,expected):
    greetUser(first,middle,last)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected


#displayItem
#first passes
#second fails -> IndexError -> out of range
#third fails -> IndexError -> should not have a negative index
#fourth fails -> TypeError -> cannot be a float
#fifth fails -> TypeError -> cannot be a string
@pytest.mark.parametrize("numbers, index,expected",[([1,5,9,8],2,"Your item at 2 index is 9"),([5,7,6,3,1],5,"Your item at 5 index is 0"),([9,6,2,1,99],-9,"Your item at -4 index is 0"),([8,7,2,8],2.5,"Your item at 2.5 index is 0"),([7,4,0,1],'1',"Your item at 1 index is 4")])
def test_displayItem(capsys,numbers,index,expected):
    displayItem(numbers,index)

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

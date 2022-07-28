# cse2213_hw5
Methods and Tools in Software Development HW5

TESTING:

Take the given Python file. Analyze the functions provided and determine what inputs could possibly cause a function to crash. Additionally, what would you expect given a possible input? All of the functions (except greetUser) have at least two distinct ways an input could crash the function. This could be due to data type or it could be due to the actual value of the variable. Once you have a correct input, you also need to verify correct things are being done with the input.

So, for instance, with greetUser, while the program won't crash, how can you test that it's working correctly?

Generate a separate Python file with PyTest tests for each of the Python functions. Each function should have THREE tests AT MINIMUM. Each function should have two distinct items to be tested (then, you could have multiple tests testing that one item; i.e., testing an input for a float and string). For instance, testing for data type crashing and testing that the math is done correctly are technically two distinct types of tests. You'll need 30 tests at minimum for the project as a whole. So, some functions may get more than the required 3 tests. (PyTest when run should register 30 distinct tests.)

(** Keep in mind, you don't have to test every part of a function. If you're testing for functionality, you don't necessarily always have to test for correct outputs at that time.)

CORRECTING:

At this point: you should have some (many) failures. Correct your Python file! Can certain tests be passed with Try/Except blocks? Is it due to input conversion? Math? Wrong values? Certain tests in here can be easily passed with a little tweaking.

** Note! greetUser in the comments says it wants to only accept names that are all letters. You should address this!

DOCUMENTATION:

While testing/correcting, keep track of what you're doing. For each function, write a few things that you think you should test. What inputs would you then use to test? List these inputs. For corrections to the Python file: document what changes you're applying. Why did you make these changes? What tests originally failed that now pass?

Additionally, do you have any tests that are meant to fail AFTER CORRECTIONS? Why are these meant to fail? What are they?

Include a screenshot of your PyTest run report in this document.

A sample document format can be found here: homework5.docx  Download homework5.docx 

(*For the document, each python function in the functions.py should have a summary like the one listed. So, you should have eight summaries total. You're not giving a summary for each PyTest function.)

Make sure you have all your members names and netIDs on the document!

Resources:

Some of my Python slides can be found here (if you need some Python help):

Files Download Files
Exceptions Download Exceptions

Deliverables:

Your PyTest python file containing your tests
The corrected Python file accounted for failures
a PDF write up of the requested items
a screen recording of PyTest being run
(must be .mkv, .mov, or .mp4)
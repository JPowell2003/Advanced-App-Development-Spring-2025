# File Name : main.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 03
# Due Date:  2/06/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Create and testing a function that checks whether a number is divisible by both 3 and 5, using a separate test script to verify its correctness.
# Brief Description of what this module does: Imports the is_divisible function from Function.py and runs five test cases to verify its correctness
# Citations:
# Anything else that's relevant:

from Function import *

count_passed = 0
count_failed = 0

#Test 1
if (is_divisible(15) == True):
    print("Test #1 passed")
    count_passed = count_passed + 1
else:
    print("Test #1 FAILED")
    count_failed = count_failed + 1

#Test 2
if (is_divisible(1) == False):
    print("Test #2 passed")
    count_passed = count_passed + 1
else:
    print("Test #2 FAILED")
    count_failed = count_failed + 1

#Test 3
if (is_divisible(5) == False):
    print("Test #3 passed")
    count_passed = count_passed + 1
else: 
    print("Test #3 FAILED")
    count_failed = count_failed + 1

#Test 4
if (is_divisible(0) == True):
    print("Test #4 passed")
    count_passed = count_passed + 1
else:
    print("Test #4 FAILED")
    count_failed = count_failed + 1

#Test 5
if (is_divisible(37) == False):
    print("Test #5 passed")
    count_passed = count_passed + 1
else:
    print("Test #5 FAILED")
    count_failed = count_failed + 1

print(str(count_passed) + " tests passed and " + str(count_failed) + " tests failed")

# File Name : Function.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 03
# Due Date:  2/06/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment:Create and testing a function that checks whether a number is divisible by both 3 and 5, using a separate test script to verify its correctness.
# Brief Description of what this module does: This module contains a function that checks whether a given integer is divisible by both 3 and 5.
# Citations:
# Anything else that's relevant:

def is_divisible(number):
    '''
    Check if the given integer is divisible by both 3 and 5.
    @param number integer: the number to check divisibility on
    @return bool: True if the integer is divisible by 3 and 5, otherwise False
    '''
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False
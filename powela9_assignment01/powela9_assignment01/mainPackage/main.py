# File Name : Jay
# Student Name: Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 01
# Due Date:  1/21/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: An introduction to Python where we tell the module it is the entry point and prints to the console
# Brief Description of what this module does: An introduction to Python where we print "Hello World!" to the console
# Citations:
# Anything else that's relevant:

from function import * #Used to drag in all code in function.py

#Need to get code from myFile which is in a second package
from SecondPackage import myFile

#Check to see if this module is the entry point
if __name__ == "__main__":
    print("Hello World")
#Use __ for system functions



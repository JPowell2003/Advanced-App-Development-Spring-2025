# File Name: powela9_assignment02
# Student Name: Jay
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 02
# Due Date: 1/30/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: 
# This assignment is on Python fundamentals, including variable assignments, type conversions, string manipulation, and mathematical operations.
#
# Brief Description of what this module does:
# This module prints my name, assigns values to variables, performs string concatenation, 
# mathematical operations, and extracts specific characters from strings. The module also 
# shows variable reassignment and type casting.
#
# Citations: N/A
# Anything else that's relevant: N/A

#Print my name to console
print("Jay Powell")

alpha = 98
print(alpha)
#alpha is an integer since it's a number with no decimals

epsilon = "UC is in the Big 12 now"
print(epsilon + str(alpha))
#epsilon is a string since it is text in quotation marks

foo = 1.5
#Foo is a float since it's a decimal
gamma = alpha + foo
print(gamma)

omega = epsilon[11]
print(">" + omega + "<")

alpha = "12345"
#The original alpha variable was written over
#alpha is now a string since it's surrounded by quotation marks
print(alpha)

zeta = int(alpha) + foo
print(zeta)
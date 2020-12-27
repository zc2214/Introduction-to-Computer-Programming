"""
Created on Fri Dec 27 10:40:34 2019

@author: hl3797
"""

# PROGRAMMING ASSIGNMENT 02
# Filename: 'exercise3.py'
#
# Write a program that does the following (in the specified order):
# 1. asks the user to input a year (type: int)
# 2. prints the message "Leap year" or "Not leap year" on a first line
# 3. then, only if applicable, prints the message "World Cup year" or "Euro Cup year" on a second line
#
# WRITE YOUR CODE AFTER THIS LINE

year = int(input('Year: '))

# Check leap year
is_leap = False
if year % 4 == 0:
    is_leap = True
if year % 100 == 0:
    is_leap = False
if year % 400 == 0:
    is_leap = True
# Simplified version of if - else
print('Leap year' if is_leap else 'Not leap year')

# Check World Cup
if year >= 1950 and (year - 1950) % 4 == 0:
    print('World Cup year')

# Check Euro Cup
if year >= 1960 and (year - 1960) % 4 == 0:
    print('Euro Cup year')

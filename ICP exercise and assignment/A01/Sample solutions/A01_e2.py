"""
Created on Mon Dec 23 21:34:13 2019

@author: hl3797
"""
# PROGRAMMING ASSIGNMENT 01
# Filename: 'exercise2.py'
#
# Write a program that does the following (in the specified order):
# 1. asks the user to input the first grade (int between 0 and 100)
# 2. asks the user to input the second grade (int between 0 and 100)
# 3. asks the user to input the third grade (int between 0 and 100)
# 4. then, prints the average grade (keep it as an integer, choose the closest integer)
#
# WRITE YOUR CODE AFTER THIS LINE

# Get grades and convert to intenger
grade1 = int(input('1st grade: '))
grade2 = int(input('2nd grade: '))
grade3 = int(input('3rd grade: '))
# Compute average grade and output
print('Average grade:', int((grade1 + grade2 + grade3) / 3 + 0.5))

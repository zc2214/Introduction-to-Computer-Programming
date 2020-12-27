"""
Created on Fri Dec 27 10:34:41 2019

@author: hl3797
"""
# PROGRAMMING ASSIGNMENT 02
# Filename: 'exercise1.py'
#
# Write a program that does the following:
# 1. asks the user to input a number (type: int)
# 2. then, prints "odd" or "even" depending on the number's parity
#
# WRITE YOUR CODE AFTER THIS LINE

num = int(input('Input a number: '))
# Odd or Even
if num % 2 == 1:
    print('odd')
else:
    print('even')

# PROGRAMMING ASSIGNMENT 03
# Filename: 'exercise2.py'
#
# Write a program that does the following:
# 1. asks the user to input a password length N (type: int, positive)
# 2. then, generates and prints a random password of N characters*
#
# *see the list of valid characters in the pdf file
#
# NOTE: you MUST use a while loop for this exercise
#
# WRITE YOUR CODE AFTER THIS LINE

import random
length = int(input('Password length:'))
i = 0
pwd = ''
while i < length:
    pwd += chr(random.randint(33, 126))
    i += 1
print(pwd)

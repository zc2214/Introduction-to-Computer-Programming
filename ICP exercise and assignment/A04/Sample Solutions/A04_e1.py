'''
Created on Sun Dec 29 14:10:28 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 04
# Filename: 'exercise1.py'
#
# Write a program which asks the user to enter a positive integer N and then
# draws an hourglass of the corresponding size (2 * N - 1 lines).
# The hourglass is obtained by drawing lines containing spaces ' ' and stars '*'.
#
# see the sample examples in the pdf file
#
# NOTE: you MUST use a for loop for this exercise
#
# WRITE YOUR CODE AFTER THIS LINE

N = int(input('Enter a positive number: '))
# Compute the scale
scale = 2 * N - 1
# Loop for 2N times
for i in range(scale + 1):
    star_num = scale - 2 * i
    # Ensure that print '*' only once
    if star_num == -1:
        continue
    # Compute the numbers of characters
    star_num = abs(scale - 2 * i)
    blank_num = (scale - star_num) // 2
    print(' ' * blank_num + '*' * star_num + ' ' * blank_num)

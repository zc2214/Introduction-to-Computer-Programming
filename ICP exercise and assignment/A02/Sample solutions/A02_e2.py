"""
Created on Fri Dec 27 10:36:19 2019

@author: hl3797
"""

# PROGRAMMING ASSIGNMENT 02
# Filename: 'exercise2.py'
#
# A software company sells a package that retails for $49.99. Quantity discounts are given according to the following table:
# Less than 10: no discount
# 10 - 19: 10% discount
# 20 - 49: 20% discount
# 50 - 99: 30% discount
# 100 or more: 40% discount
#
# Write a program that does the following:
# 1. asks the user to input the number of packages he wants to buy (type: int)
# 2. then, prints the total amount of the purchase after discount
# NOTE: the total amount should keep two decimal places
#
# WRITE YOUR CODE AFTER THIS LINE

num = int(input('Number of packages: '))
price = 49.99

# Check discount intervals
if num < 10:
    print(price * num)
elif 10 <= num <= 19:
    print('%.2f' % (price * num * 0.9))
elif 20 <= num <= 49:
    print('%.2f' % (price * num * 0.8))
elif 50 <= num <= 99:
    print('%.2f' % (price * num * 0.7))
else:
    print('%.2f' % (price * num * 0.6))

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

num = int(input("Number of packages: "))
price = 49.99
if num < 10:
    total = num * price
elif 10 <= num <= 19:
    total = num * price * 0.9
elif 20 <= num <= 49:
    total = num * price * 0.8
elif 50 <= num <= 99:
    total = num * price * 0.7
else:
    total = num * price * 0.6
print('%.2f' % (total))


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


first=input("Please enter your first grade")
second=input("Please enter your second grade")
third=input("Please enter your third grade")
average=(int(first)+int(second)+int(third))/3
average=int(average)
print ("Your average grade is:",average)

# PROGRAMMING ASSIGNMENT 04
# Filename: 'exercise1.py'
#
# Write a program which asks the user to enter a positive integer N and then
# draws a diamond of the corresponding size (2 * N - 1 lines).
# The diamond is obtained by drawing lines containing spaces ' ' and stars '*'.
#
# see the sample examples in the pdf file
#
# NOTE: you MUST use a for loop for this exercise
#
# WRITE YOUR CODE AFTER THIS LINE

num = int(input("Enter a positive number:"))
if num > 1:
    print((num-1)*" "+"*"+(num-1)*" ")
    for i in range(-num+2,num-1):
        print(abs(i)*" "+"*"+(2*(num-abs(i))-3)*" "+"*")
    print((num-1)*" "+"*"+(num-1)*" ")
else:
    print("*")

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
for i in range(scale + 1,0,-1):
    space = 0.5*(2*N-1-i)
    intspace = int(space)
    if i%2 != 0:
        print(intspace*" ", i*"*", intspace*" ")
for i in range(scale + 1):
    space = 0.5*(2*N-1-i)
    intspace = int(space)
    if i%2 != 0 and i !=1:
        print(intspace*" ", i*"*", intspace*" ")

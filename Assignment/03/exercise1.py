# PROGRAMMING ASSIGNMENT 03
# Filename: 'exercise1.py'
#
# Write a program that does the following:
# • continuously asks the user to input a score which is an integer between 0 and 100 (inclusive)...
# • ...until the user enters a correct number (display a message if the user did not enter a correct number)
# • then finally prints the corresponding grade
#
# see the TABLE OF CORRESPONDENCES SCORE/GRADE in the pdf file
#
# WRITE YOUR CODE AFTER THIS LINE
loop = True
while loop:
    score = float(input('Score: '))
    if 0 <= score <= 100:
        loop = False
    else:
        print('Invalid input. Please enter a score between 0 and 100.')
if score >= 95:
    grade = 'A'
elif score >= 90:
    grade = 'A-'
elif score >= 87:
    grade = 'B+'
elif score >= 83:
    grade = 'B'
elif score >= 80:
    grade = 'B-'
elif score >= 77:
    grade = 'C+'
elif score >= 73:
    grade = 'C'
elif score >= 70:
    grade = 'C-'
elif score >= 67:
    grade = 'D+'
elif score >= 63:
    grade = 'D'
else:
    grade = 'F'
print('Your grade is', grade)
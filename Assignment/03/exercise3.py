# PROGRAMMING ASSIGNMENT 03
# Filename: 'exercise3.py'
#
# Password checker
# In order to be valid your password must have at least one of each: lower case letter, 
# upper case letter, digit and special character. 
# Write a program in the file exercise3.py that does the following:
# 	- asks the user to \textbf{input a password}
#	- then, prints: "This password is valid" if the password fulfills the conditions 
# 	  and prints: " This password is not valid" otherwise. 
# 
#
# WRITE YOUR CODE AFTER THIS LINE

pwd = input("Enter a password:")
valid = False
lower = False
upper = False
special = False
digit = False
i = 0
loop = True
while loop:
    ch = pwd[i]
    if 33 <= ord(ch) <= 47 or 58 <= ord(ch) <= 64 or 91 <= ord(ch) <= 96 or 123 <= ord(ch) <= 126:
        special = True
    elif 48 <= ord(ch) <= 57:
        digit = True
    elif 65 <= ord(ch) <= 90:
        upper = True
    elif 97 <= ord(ch) <= 122:
        lower = True
    if lower == True and upper == True and special == True and digit == True:
        valid = True
        loop = False
    if i == len(pwd) -1:
        loop = False
    i += 1
if valid == True:
    print("This password is valid")
else:
    print("This password is not valid")
    
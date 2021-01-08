# PROGRAMMING ASSIGNMENT 05
# Filename: 'exercise2.py'
#
# Write the code for function valid_password.
# The function valid_password:
#   • takes 1 parameter pwd -> type str: password
#   • displays a message (depending on password rules (see the pdf))
#   • returns if the password is valid -> type bool
#
# see the rules in the pdf file
#

def main():
    #try to check some passords
    print('Calling: valid_password(\'qwertyuiop\')')
    r = valid_password('qwertyuiop') #also catch the returned value
    print(r) #print the returned value
    
    #empty line
    print()
    
    print('Calling: valid_password(\'ICPSpring2019\')')
    r = valid_password('ICPSpring2019') #also catch the returned value
    print(r) #print the returned value
    
    #empty line
    print()
    
    print('Calling: valid_password(\'pwd!!!\')')
    r = valid_password('pwd!!!') #also catch the returned value
    print(r) #print the returned value
    
    #empty line
    print()
    
    print('Calling: valid_password(\'PWD01_#PWD01\')')
    r = valid_password('PWD01_#PWD01') #also catch the returned value
    print(r) #print the returned value


def valid_password(pwd):
    # WRITE YOUR CODE HERE

    # Initialize variables
    lenth = len(pwd)
    upper_count = 0
    lower_count = 0
    num_count = 0

    # Count characters
    for ch in pwd:
        if 'A' <= ch <= 'Z':
            upper_count += 1
        elif 'a' <= ch <= 'z':
            lower_count += 1
        elif '0' <= ch <= '9':
            num_count += 1

    # Check whether the password is valid
    if lenth < 10:
        print('Password is too short')
        return False
    elif lenth != upper_count + lower_count + num_count:
        print('Wrong characters')
        return False
    elif upper_count == 0 or lower_count == 0 or num_count == 0:
        print('Need at least 1 uppercase letter, 1 lowercase letter and 1 digit')
        return False
    else:
        print('Valid password')
        return True



#Call the main() function
main()

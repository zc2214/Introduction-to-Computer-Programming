# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise2.py'
#
# See instructions in pdf file
#
# DO NOT EDIT THE main() function
#

def main():
    """Program to check if the 3 functions work.
    The tested functions are:
    • valid_username
    • valid_password
    • add_user"""
    #create a list of users (userList)
    userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'], \
    ['likeA', 'pwd3AAAAAA'], ['qwerty', 'pwd4QWERTY']]
    print('List of users (userList):')
    print(userList)

    print()

    print('Calling: valid_username(\'user\', userList)')
    r = valid_username('user', userList) #also catch the returned value
    print(r) #print the returned value

    print()

    print('Calling: valid_password(\'azertyuiop\')')
    r = valid_password('azertyuiop') #also catch the returned value
    print(r) #print the returned value

    print()

    print('Calling: valid_password(\'12345AZERTYuiop\')')
    r = valid_password('12345AZERTYuiop') #also catch the returned value
    print(r) #print the returned value

    print()

    print('Calling: add_user(userList)')
    add_user(userList)

    print()

    print('Check if userList was updated')
    print(userList)


def valid_username(user, L):
    """
    • inputs: 1 parameter user -> type str - username
          1 parameter L -> type list (of lists) - userList
    • display a message depending on username rules (see below)
    • return: if the username is valid -> type bool

    Valid username rules are:
    • The username is made of at least 4 characters
    • It only contains alphanumeric characters (no space, no underscore, ...)
    • Case-sensitive
    • The first character cannot be a digit
    • The username does not exist in the userList

    The printed out message/returned value will be:
    • Invalid / False if the format is not correct
    • User Name Exists / False if the username already exists
    • Valid / True if all the rules are respected"""
    #WRITE YOUR CODE HERE
    if len(user)>=4 and user.isalnum() and user[0].isalpha:
        if user in L:
            print('User Name Exists')
            return False
        else:
            print('Valid')
            return True
    else:
        print('Invalid')
        return False




def valid_password(pwd):
    """
    • input: 1 parameter pwd -> type str - password
    • displays a message depending on password rules (see below)
    • return: if the password is valid -> type bool

    Valid password rules are:
    • The password is made of at least 10 characters
    • It only contains alphanumeric characters (no space, no underscore, ...)
    • There is at least:
        - 1 uppercase character
        - 1 lowercase character
        - 1 digit

    The printed out message/returned value will be:
    • Invalid / False if the password is not correct
    • Valid / True if all the rules are respected"""
    #WRITE YOUR CODE HERE
    upper_count = 0
    lower_count = 0
    num_count = 0
    for ch in pwd:
        if ord("A") <= ord(ch) <= ord("Z"):
            upper_count = upper_count +1
        elif ord("a") <= ord(ch) <= ord("z"):
            lower_count = lower_count +1
        elif ord("0") <= ord(ch) <= ord("9"):
            num_count = num_count +1
    if len(pwd) == upper_count + lower_count + num_count and upper_count>=1 and lower_count>=1 and num_count>=1:
        print('Valid')
        return True
    else:
        print('Invalid')
        return False        


def add_user(L):
    """
    • input: 1 parameter L -> type list (of lists) - userList
    • adds a username/password pair to the userList
    • return: nothing

    The function should:
    1. continuously ask the user to input a username, until it is a valid one
    2. ask for a password with the following logic:
        (a) continuously ask the user to input a password, until it is a valid one
        (b) ask the user to input the password again:
            • if the 2 passwords match -> move to 3.
            • otherwise -> display Passwords do not match and go back to 2.(a)
    3. add the username/password pair to the userList and display User created"""
    #WRITE YOUR CODE HERE
    username = input('Enter Username: ')
    while not valid_username(username, L):
        username = input('Enter Username: ').strip()
    while True:
        userpwd = input('Enter Password: ').strip()
        while not valid_password(userpwd):
            userpwd = input('Enter Password: ').strip()
        confirm_pwd = input('Confirm Password: ')
        if confirm_pwd == userpwd:
            break
    print(username, userpwd)
    L.append([username, userpwd])
    print('User created')




#Call the main() function
main()

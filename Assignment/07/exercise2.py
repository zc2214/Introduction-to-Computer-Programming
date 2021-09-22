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
    """• inputs: 1 parameter user -> type str - username
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
    is_valid = True
    is_exist = False
    for j in L:
        if user == j[0]:
            print("User Name Exists")
            is_exist = True
    if len(user) < 4:
        is_valid = False
    for i in user:
        if i.isalpha() == False and i.isnumeric() == False:
            is_valid = False
    if ord(user[0]) in range(48,58):
        is_valid = False
    if is_valid == False and is_exist == False:
        print("Invalid")
    elif is_valid == True and is_exist == False:
        print("Valid")
    if is_exist == True or is_valid == False:
        return False
    else:
        return True
    
    

def valid_password(pwd):
    """• input: 1 parameter pwd -> type str - password
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
    is_valid = True
    upper = False
    lower = False
    digit = False
    if len(pwd) < 10:
        is_valid = False
    for i in pwd:
        if i.isalpha() == False and i.isnumeric() == False:
                is_valid = False
        if ord(i) in range(65,91):
            upper = True
        if ord(i) in range(97,123):
            lower = True
        if ord(i) in range(48,58):
            digit = True
    if upper == False or lower == False or digit == False:
        is_valid = False
    if is_valid == False:
        print("Invalid")
        return False
    else:
        print("Valid")
        return True

    
def add_user(L):
    """• input: 1 parameter L -> type list (of lists) - userList
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
    user_loop = True
    pwd_loop = True
    while user_loop:
        user = input("Enter Username: ")
        if valid_username(user, L) == True:
            user_loop = False
    while pwd_loop:
        pwd = input("Enter Password: ")
        if valid_password(pwd) == True:
            con_pwd = input("Confirm Password: ")
            if con_pwd == pwd:
                pwd_loop = False
                print("User created")
            else:    
                print("Passwords do not match")
    L += [[user,pwd]]
    
    


#Call the main() function
if __name__ == '__main__':
    main()

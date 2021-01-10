'''
Created on Sun Dec 29 15:24:06 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    1) asks the user to input 5 usernames (only alphanumeric characters will be input,
       no space, no underscore, ...) and stores them into a list
    2) prints out the list of usernames
    3) calls clean_users function to clean the list
    4) prints out the cleaned list"""
    #WRITE YOUR PROGRAM HERE

    # Initialize user list and get input
    user_ls = []
    for i in range(5):
        user_ls.append(input('username: ').strip())
    print(user_ls)

    # Call the function and output new list
    clrd_user_ls = clean_users(user_ls)
    print(clrd_user_ls)



def clean_users(L):
    """
    • input: 1 parameter L -> type list (of strings) - each element in the list is a username
    • return: a new cleaned list (see the rules below) -> type list (of strings)

    The logic for cleaning the list of usernames is:
    • if the username contains c, g or z, it should be removed (the same with C, G or Z)
    • otherwise, keep it in the list

    Note: your function should not modify the original list!"""
    #WRITE YOUR CODE HERE

    # Copy the original list
    user_ls = L[:]
    # Loop through original list and modify new list
    for username in L:
        # Convert usernames to lowercase
        lc_name = username.lower()
        if ('c' in lc_name) or ('g' in lc_name) or ('z' in lc_name):
            # Remove some of the users
            user_ls.remove(username)
    return user_ls


#Call the main() function
main()

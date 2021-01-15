'''
Created on Sun Dec 29 16:55:04 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 07
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    - it inserts all the content from file2.txt to the beginning of file1.txt

    Note: After execution of the your program, only file1.txt is updated, file2.txt does not change."""
    #WRITE YOUR PROGRAM HERE

    try:
        # Get the content of file1.txt
        f1 = open('file1.txt', 'r')
        txt1 = f1.read()
        f1.close()

        # Get the content of file2.txt
        f2 = open('file2.txt', 'r')
        txt2 = f2.read()
        f2.close()

        # Update the content of file1.txt
        f1 = open('file1.txt', 'w')
        f1.write(txt2 + txt1)
        f1.close()

    except Exception as err:
        # Handle exceptions
        print(err)


#Call the main() function
main()

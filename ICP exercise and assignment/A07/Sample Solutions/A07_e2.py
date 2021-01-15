'''
Created on Sun Dec 29 17:04:59 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 07
# Filename: 'exercise2.py'
#
# See instructions in pdf file
#

import os

def main():
    """The program does the following:
    1) asks the user to input a filename (supposedly in the same folder as this program)
	2) reads the numbers (type int) in the file (filename given by the user in previous step) and stores them into a list
	3) prints the minimum, the maximum and the average of the numbers (2 decimal places for the average)

    Note: your program should be impossible to crash. Think about all the possibilities to make your program crash.
    If one of the steps throws an exception, display a message to the user and your program should loop back to step 1."""
    #WRITE YOUR PROGRAM HERE

    try:
        # Get file list of current path
        file_ls = os.listdir('./')
        while True:
            # Get filename
            filename = input('Filename:\n').strip()
            while filename == '':
                print('Invalid filename\n')
                filename = input('Filename:\n').strip()
            # Check whether filename is in the list
            if filename in file_ls:
                # Create a valid data list and read the data
                data_num_ls = []
                data_str_ls = open(filename, 'r').read().split('\n')
                # Flag for existing other data type in the file
                other_type_flag = False
                for item in data_str_ls:
                    # Only compute int data
                    if item != '' and item.isdigit():
                        data_num_ls.append(int(item))
                    else:
                        print('Invalid data:', item)
                        other_type_flag = True
                # Exception for no valid data
                if len(data_num_ls) == 0:
                    print('There\'s no valid data could be computed\n')
                else:
                    # Output
                    if other_type_flag:
                        print('Note: non-int data has been omitted')
                    print('Minimum:', min(data_num_ls))
                    print('Maximum:', max(data_num_ls))
                    print('Average: %.2f' % (sum(data_num_ls) / len(data_num_ls)))
                    print()
            else:
                # Exception of 'No such a file'
                print('File not found\n')
    except Exception as err:
        # Handle other exceptions
        print(err)


#Call the main() function
main()

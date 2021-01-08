'''
Created on Sun Dec 29 15:07:26 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 05
# Filename: 'exercise1.py'
#
# Write the code for function diamond.
# The function diamond:
#   • takes one parameter N (type int), its value must be odd and in the range [3, 99]
#   • it draws a square shape made of integer values and spaces:
#       - integer values are always printed with 2 digits (for example, value 7 is printed 07)
#       - every line consists of integer values from 1 up to N , where some values have to be
#       replaced by spaces instead
#       - the first and last row are full (no space)
#       - the middle row is empty except for values 1 and N ,
#       - each row from the FIrst one to the middle one is increasingly empty from its center
#       - each row from the middle one to the last one is increasingly full to its center

def main():
    #try to draw some diamonds by calling the function diamond
    print('Calling: diamond(5)')
    diamond(5)

    #empty line
    print()

    print('Calling: diamond(15)')
    diamond(15)


def diamond(N):
    #WRITE YOUR CODE HERE

    # Compute the scale
    key = (N + 1) // 2

    for i in range(1, N + 1):
        # Initialize variables and compute the numbers
        num = 1
        line = ''
        blank_count = N - 2 - 2 * abs(key - i)
        num_count = (N - blank_count) // 2

        # Generate the output of one line
        for i in range(num_count):
            line += '%02d' % num
            num = num + 1
        for i in range(blank_count):
            line += '  '
            num = num + 1
        for i in range(num_count):
            # Handle the exception of first and last lines
            if num <= N:
                line += '%02d' % num
                num = num + 1

        # Output
        print(line)

#Call the main() function
main()

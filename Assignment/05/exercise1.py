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
    for i in range( -(N+1)//2, (N+1)//2+1):
        if i != 0 and i != 1:
            temp_str = ""
            for j in range(1,N+1):
                if abs(i) >= j or ((N+1)-abs(i)) <= j:
                    temp_str += str(j).zfill(2)
                else:
                    temp_str += "  "
            print(temp_str)

    


#Call the main() function
if __name__ == '__main__':
    main()
# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise2.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    1) asks the user to input a filename (supposedly in the same folder as this program)
	2) reads the numbers (type int) in the file (filename given by the user in previous step) and stores them into a list
	3) prints the minimum, the maximum and the average of the numbers (2 decimal places for the average)
    
    Note: your program should be impossible to crash. Think about all the possibilities to make your program crash.
    If one of the steps throws an exception, display a message to the user and your program should loop back to step 1."""
    #WRITE YOUR PROGRAM HERE
    loop = True
    while loop:
        file_name = input("Filename:")
        try:
            f = open(file_name,"r")
        except:
            print("File not found")
            continue
        file_list = f.read().split()
        f.close()
        int_list = []
        try:
            for i in file_list:
                int_list += [int(i)]
        except:
            print("not int inside")
            continue
        print("Minimum: " + str(min(int_list)))
        print("Maximum: " + str(max(int_list)))
        print("Average: " + "{:.2f}".format(sum(int_list)/len(int_list)))
            


    

#Call the main() function
if __name__ == '__main__':
    main()
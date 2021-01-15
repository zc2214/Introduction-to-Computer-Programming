# PROGRAMMING ASSIGNMENT 07
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
    name = input("pls enter file's name")
    extend = ".txt"
    filename = name + extend
    try:
        file = open(filename, "r")    
    except:
        print("Not Found")
    else:
        l = file.read().split()
        L = []
        for i in l:
            i = int(i)
            L = L + [i]
        maxm = max(L)
        minm = min(L)
        summ = sum(L)
        avg = summ/(len(L))
        print("Minimum:",minm)
        print("Maximum:",maxm)
        print("Average:",avg)
        file.close()
        

#Call the main() function
main()

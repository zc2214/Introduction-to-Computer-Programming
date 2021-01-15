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
    file1 = open("file1.txt","a")
    file2 = open("file2.txt","r")
    L = file2.readlines()
    file1.write("\n")
    for i in L:
        file1.write(i)
    file1.close()
    file2.close()
        
#Call the main() function
main()

# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def main():
    """The program does the following:
    - it inserts all the content from file2.txt to the beginning of file1.txt
    
    Note: After execution of the your program, only file1.txt is updated, file2.txt does not change."""
    #WRITE YOUR PROGRAM HERE
    f1 = open("file1.txt","r")
    f2 = open("file2.txt","r")
    str1 = f1.read()
    str2 = f2.read()
    f1.close()
    f2.close()
    f = open("file1.txt","w")
    f.write(str2+str1)
    f.close()

    

#Call the main() function
if __name__ == '__main__':
    main()
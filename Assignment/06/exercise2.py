# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# Titles of books or articles generally capitalize the first letter of every important 
# word.  The first and last word are always capitalized.The following words should not be 
# capitalized: a, an, the, at, by, for, in, of, on, to, up, and, as, but, or, and nor.
#You must write a function named title_case that capitalizes the appropriate characters 
# in a string. Include a main program that reads a string from the user, capitalizes it 
# using your function, and displays the result. 



    

def title_case(title):
    #WRITE YOUR CODE HERE
    new_str = ""
    for i in range(0,len(title)-1):
        if title[i] == " ":
            j = title.find(" ",i+1)
            temp_str = ""
            for k in range(i+1,j):
                temp_str += title[k]
            if temp_str == "a" or temp_str == "an" or temp_str == "the" or temp_str == "at" or temp_str == "by" or temp_str == "for" or temp_str == "in" or temp_str == "of" or temp_str == "on" or temp_str == "to" or temp_str == "up" or temp_str == "and" or temp_str == "as" or temp_str == "but" or temp_str == "or" or temp_str == "nor" or temp_str.isnumeric == True:
                new_str += temp_str
            else:
                upper_str = ""
                for a in range(0,len(temp_str)):
                    if a == 0:
                        upper_str += temp_str[0].upper()
                    else:
                        upper_str += temp_str[a]
                new_str += upper_str
            new_str += " "
    new_str = new_str.strip(" ")
    for m in range(0,len(title)-1):
        if title[m] == " ":
            last_space = m
    first_word_upper = title[0].upper()
    last_word_upper = title[last_space+1].upper()
    x = title.find(" ")
    for y in range(1,x):
        first_word_upper += title[y]
    new_str = first_word_upper + " " + new_str
    for z in range(last_space+2,len(title)):
        last_word_upper += title[z]
    new_str = new_str + " " + last_word_upper
    new_new_str = "Here is your title: " + new_str
    return new_new_str

        

    
    
def main():
    title = input("Enter a title to be formatted:")
    print(title_case(title))

#Call the main() function
if __name__ == '__main__':
    main()
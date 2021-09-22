# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# An anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once. Spaces and punctuation 
# are not taken into consideration. 
# You should write two functions. The first one called check_anagrams takes two parameters 
# (strings) checks whether the two string are anagrams of each other. check_anagrams 
# returns True if the two strings are anagrams and False otherwise. The main function 
# should ask the user to enter two strings and prints the result by calling the other 
# function check_anagrams.


    

def check_anagrams(S1, S2):
    #WRITE YOUR CODE HERE
    def check_anagram(a,b):
        for i in a:
            if ord(i.lower()) in range(97,123):
                if a.lower().count(i) == b.lower().count(i):
                    continue
                else:
                    return False
    if check_anagram(S1,S2) == False or check_anagram(S1,S2) == False:
        return False
    else:
        return True
    
    
def main():
    s1 = input("Enter the first word or phrase:")
    s2 = input("Enter the second word or phrase:")
    if check_anagrams(s1,s2) == True:
        print('"'+s1+'", and "'+s2+'" '+"are anagrams.") 
    elif check_anagrams(s1,s2) == False:
        print('"'+s1+'", and "'+s1+'" '+"are not anagrams.") 

#Call the main() function
if __name__ == '__main__':
    main()
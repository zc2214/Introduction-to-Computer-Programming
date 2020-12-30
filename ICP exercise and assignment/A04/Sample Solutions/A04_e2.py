'''
Created on Sun Dec 29 14:24:30 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 04
# Filename: 'exercise2.py'
#
# Write a program that does the following:
# 1. Generate a random number between 3 and 6, inclusive - this will determine how many words to ask for
# 2. Display: I'll need [number] words:
# 3. Proceed to ask for each word, one at a time: Word \#[number] please >
# 4. At the end, your program should print out:
#       (a) the longest word (the most recently entered longest if there is a tie)
#       (b) the shortest word (the most recently entered shortest if there is a tie)
#       (c) the average length of all of the words (up to the second decimal point)
#
# see the sample examples in the pdf file
#
# NOTE: you MUST use a for loop for this exercise
#
# WRITE YOUR CODE AFTER THIS LINE

from random import randint

# Initialize variables
N = randint(3, 6)
min_length = float('inf')
max_length = 0
sum_length = 0
max_word = ''
min_word = ''
print('I\'ll need', N, 'words:')

for i in range(N):
    word = ''
    # Ensure the input is valid
    while word == '':
        word = input('Word #' + str(i + 1) + ' please > ').strip()
    # Accumulate length and update variables
    sum_length += len(word)
    if len(word) >= max_length:
        max_length = len(word)
        max_word = word
    if len(word) <= min_length:
        min_length = len(word)
        min_word = word

# Output results
print('Shortest:', min_word)
print('Longest:', max_word)
print('Average Length: %.2f' % (sum_length / N))

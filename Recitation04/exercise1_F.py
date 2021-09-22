total_bugs = 0  #total number of bugs

#repeat until we have entered bugs for 5 days
for days in range(5):
    bugs = int(input('How many bugs today?\n> '))
    total_bugs += bugs   #add to the total

#out of the loop: meaning we have collected bugs for 5 days
print()     #blank line
print('Total Number of Bugs:', total_bugs)

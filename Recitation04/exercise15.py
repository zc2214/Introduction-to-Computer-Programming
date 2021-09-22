import random

#sentinel variable with 'fake' initial value to enter the loop the first time
n = 'anything'

keepGoing = True

while keepGoing:
    n = int(input('Password size? > '))

    if n == 0:      #terminate the loop immediately
        keepGoing = False

    i = 0
    while i < n:
        digit = random.randint(0,9)
        print(digit,end='') #no line break
        i += 1

    print()     #line break

n = 5

for i in range(n):          #will display until (n-1) stars
    for j in range(i):
        print('* ',end='') #no line break

    print()     #line break

for i in range(n,0,-1):     #will display from n to 1 stars
    for j in range(i):
        print('* ',end='') #no line break

    print()     #line break



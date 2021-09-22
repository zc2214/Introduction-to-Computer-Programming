N = int(input('Number of triangles?\n> '))
M = int(input('Size?\n> '))

for i in range(N):      #repeat for each triangle
    for j in range(1,M+1):          #will display from 1 to M stars
        for k in range(j):
            print('* ',end='') #no line break
        print()     #line break
        

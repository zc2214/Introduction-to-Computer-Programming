N = int(input('Enter a strictly positive integer: '))

x, y = 0, 1

print(x)
for i in range(1,N+1):
    print(y)
    x, y = y, (x + y)

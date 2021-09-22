c1 = input('First color:\n> ')

if c1 == 'red':
    n1 = 1
elif c1 == 'blue':
    n1 = 2
elif c1 == 'yellow':
    n1 = 5
else:
    n1 = -100

c2 = input('Second color:\n> ')

if c2 == 'red':
    n2 = 1
elif c2 == 'blue':
    n2 = 2
elif c2 == 'yellow':
    n2 = 5
else:
    n2 = -100

result = n1 + n2

if result < 0:
    print('ERROR')
elif n1 == n2:
    print(c1)
elif result == 3:
    print('purple')
elif result == 6:
    print('orange')
else:
    print('green')

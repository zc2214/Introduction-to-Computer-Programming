n = int(input('Enter a positive integer\n> '))

factorial = 1

#the trick is to start from n, then multiply by (n-1), and so on...
while n > 1: #can also be >= 1
    factorial *= n
    n -= 1              #decrement n value by 1 for next multiplication

print('Factorial is:', factorial)

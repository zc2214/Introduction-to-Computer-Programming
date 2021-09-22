n = int(input('Enter a positive integer\n> '))

factorial = 1

for i in range(1,n+1): #(n+1) in range object to include value n
    factorial *= i

print('Factorial is:', factorial)

#def functions
def is_prime(number):
    prime = True
    for i in range(2,number):
        if number % i ==0:
            prime = False
            break
    return prime

#main program
for number in range(1,101):
    print('Number ' + str(number) + ' is ' + (not is_prime(number))*'not ' + 'prime')

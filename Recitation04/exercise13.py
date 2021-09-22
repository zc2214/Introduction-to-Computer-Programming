for i in range(1,101): #numbers from 1 to 100
    if (i % 5 == 0) and (i % 3 == 0):   #multiple of 3 and 5 (could be replaced by multiple of 15)
        print('FizzBuzz')
    elif (i % 3 == 0):                  #multiple of 3 but not 5
        print('Fizz')
    elif (i % 5 == 0):                  #multiple of 5 but not 5
        print('Buzz')
    else:                               #not multiple of 3 or 5
        print(i)

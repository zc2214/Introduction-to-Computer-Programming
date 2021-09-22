celsius = 0         #sentinel variable

#header print
print('Celsius\tFahrenheit')

while celsius <=20:
    farhenheit = 9 / 5 * celsius + 32
    #print(' ' + str(celsius) + '\t ' + str(farhenheit))

    #another solution to get a proper rounded display
    print(' ' + str(celsius) + '\t ' + '%1.1f' % farhenheit)

    celsius +=1

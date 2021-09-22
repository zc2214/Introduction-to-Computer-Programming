number = int(input('Enter a number between 1 and 10\n> '))

print()     #blank line

if number<1 or number>10:
    print('Error: Number outside the range 1-10')
else:
    if number==1:
        roman = 'I'
    elif number==2:
        roman = 'II'
    elif number==3:
        roman = 'III'
    elif number==4:
        roman = 'IV'
    elif number==5:
        roman = 'V'
    elif number==6:
        roman = 'VI'
    elif number==7:
        roman = 'VII'
    elif number==8:
        roman = 'VIII'
    elif number==9:
        roman = 'IX'
    else:   #number is 10
        roman = 'X'
    print('The roman numeral version of', number, 'is',roman)

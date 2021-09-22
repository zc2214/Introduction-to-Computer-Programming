num = int(input('Enter a number between 1 and 10\n> '))

print()     #blank line

if (num<=0) or (num>10):
    print('ERROR')
elif num<=3:
    print('I'*num)
elif num==4:
    print('IV')
elif num<=8:
    print('V' + 'I'*(num-5))
else:
    print((10-num)*'I' + 'X')


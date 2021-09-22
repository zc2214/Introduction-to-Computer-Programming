number_cookies = int(input('How many cookies you want to make?\n> '))

sugar = number_cookies * 1.5 / 48
butter = number_cookies * 1 / 48
flour = number_cookies * 2.75 / 48

print('You need:')
print('\t' + str(sugar) + ' cups of sugar')
print('\t' + str(butter) + ' cups of butter')
print('\t' + str(flour) + ' cups of floor')

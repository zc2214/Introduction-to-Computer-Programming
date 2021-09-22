print('The primary colors are:')
print('\tred \tblue \tyellow\n')

color1 = input('Enter the 1st primary color: ')
color2 = input('Enter the 2nd primary color: ')

if color1==color2:
    if color1=='red' or color1=='blue' or color1=='yellow':
        print('Same color:',color1)
    else:
        print('Error: you did not enter proper primary color')
elif (color1=='red' or color2=='red') and (color1=='blue' or color2=='blue'):
    print('Secondary color is: purple')
elif (color1=='red' or color2=='red') and (color1=='yellow' or color2=='yellow'):
    print('Secondary color is: orange')
elif (color1=='blue' or color2=='blue') and (color1=='yellow' or color2=='yellow'):
    print('Secondary color is: green')
else:
    print('Error: you did not enter proper primary color')

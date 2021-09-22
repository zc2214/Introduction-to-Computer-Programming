print('Rectangle 1:')
length_rect1 = float(input('\tLength? > '))
width_rect1 = float(input('\tWidth?  > '))

print('Rectangle 2:')
length_rect2 = float(input('\tLength? > '))
width_rect2 = float(input('\tWidth?  > '))

area_rect1 = length_rect1 * width_rect1
area_rect2 = length_rect2 * width_rect2

print()     #blank line

if area_rect1>area_rect2:
    print('Rectangle 1 has the greater area')
elif area_rect2>area_rect1:
    print('Rectangle 2 has the greater area')
else:
    print('Areas are the same')

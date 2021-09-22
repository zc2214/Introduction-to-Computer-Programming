w1 = int(input('Enter WIDTH for rectangle 1:\n> '))
l1 = int(input('Enter LENGTH for rectangle 1:\n> '))

area1 = w1 * l1

w2 = int(input('Enter WIDTH for rectangle 2:\n> '))
l2 = int(input('Enter LENGTH for rectangle 2:\n> '))

area2 = w2 * l2

if area1 > area2:
    print('Rectangle 1 has the greater area')
elif area1 < area2:
    print('Rectangle 2 has the greater area')
else:
    print('Both rectangles have the same area')

l = []

for i in range(7):
    l.append(float(input('Sales of the day: ')))

total_sales = 0

for sale in l:
    total_sales += sale

print('Total sales:',total_sales)

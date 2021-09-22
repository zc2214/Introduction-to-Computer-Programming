def main():
    days = ('Monday','Tuesday', \
            'Wednesday','Thursday', \
            'Friday','Saturday', \
            'Sunday')

    #initialize list with zeros
    sales = [0] * len(days)
    
    for i in range(len(days)):
        sales[i] = int(input('Sales on {0}?\n> '.format(days[i])))

    total = 0
    for sale in sales:
        total += sale

    print('\nTotal sales: {0}'.format(total))

#Call main
main()

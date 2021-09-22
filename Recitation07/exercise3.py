import random

def main():
    num = 20
    range_min = 1
    range_max = 100

    #initialize list with zeros
    list_num = [0] * num

    print('Generating {0} random numbers between {1} and {2}...'.format(num,range_min,range_max))
    for i in range(num):
        list_num[i] = random.randint(range_min, range_max)

        total = 0
    for item in list_num:
        total += item

    average = total / num

    print('\nLowest number: {0}'.format(min(list_num)))
    print('\nHighest number: {0}'.format(max(list_num)))
    print('\nTotal: {0}'.format(total))
    print('\nAverage: {0}'.format(average))


#Call main
main()

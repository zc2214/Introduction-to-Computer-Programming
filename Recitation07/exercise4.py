import random

def main():
    num = int(input('How many numbers you want to generate?\n> '))
    range_min = int(input('Minimum value for random range?\n> '))
    range_max = int(input('Maximum value for random range?\n> '))

    #initialize list with zeros
    list_num = [0] * num

    print('Generating {0} random numbers between {1} and {2}...'.format(num,range_min,range_max))
    for i in range(num):
        list_num[i] = random.randint(range_min, range_max)

    value = int(input('You want to display the numbers greater than? '))

    greater_than(list_num, value)

def greater_than(list, n):
    for number in list:
        if number > n:
            print(number)

#Call main
main()

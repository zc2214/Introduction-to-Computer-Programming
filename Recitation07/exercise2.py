import random

def main():
    num_digits = 7

    #initialize list with zeros
    lottery_number = [0] * num_digits

    for i in range(num_digits):
        lottery_number[i] = random.randint(0,9)

    for i in range(num_digits):
        print(lottery_number[i],end='')


#Call main
main()

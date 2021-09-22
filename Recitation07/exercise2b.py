import random

def main():
    l = []

    for i in range(7):
        l.append(random.randint(0,9))

    for n in l:
        print(n, end='')



main()

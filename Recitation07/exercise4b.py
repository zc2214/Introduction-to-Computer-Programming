import random

def main():
    l = []

    for i in range(50):
        l.append(random.randint(1,100))

    print(l)

    n = int(input('Display numbers larger than: '))

    larger_than_n(l, n)

    print(l)


def larger_than_n(l_, n_):
    for m in l_[:]:
        if m > n_:
            l_.remove(m)
    



main()

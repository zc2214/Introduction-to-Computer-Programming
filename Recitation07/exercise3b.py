import random

def main():
    l = []
    for i in range(20):
        l.append(random.randint(1,100))

    print(l)
    print(min(l))
    print(max(l))
    print(sum(l))
    print(sum(l)/len(l))
    






main()

import random

def main():
    f = open('chinese-provincial-capitals.txt', 'r')

    #GET RID OF FIRST LINE
    f.readline()

    d={}
    for line in f:
        l = line.split(',')
        d[l[0]] = l[1].rstrip()

    f.close()

    provinces = list(d.keys())
    right_a = 0
    wrong_a = 0
    
    while len(provinces) > 0:
        province = random.choice(provinces)
        print(province)
        user=input('Capital: ')

        if user.lower() == d[province].lower():
            right_a += 1
        else:
            wrong_a += 1

        print('Right answers:',right_a)
        print('Wrong answers:',wrong_a)
        print()

        provinces.remove(province)






main()

import random

def main():
    f = open('chinese-provincial-capitals.txt', 'r')

    #line to read the first line (but I don't do anything with it)
    f.readline()

    chinese_capitals = {}

    for s in f:
        s = s.rstrip('\n')
        l = s.split(',')
        chinese_capitals[l[0]] = l[1]

    f.close()

    list_of_provinces = list(chinese_capitals.keys())
    correct = 0
    incorrect =0

    while True:
        province = random.choice(list_of_provinces)

        answer = input('What is the Capital of ' + province + '?\n> ')

        if answer == '0':
            break

        if answer.lower() == chinese_capitals[province].lower():
            print('Correct')
            correct += 1
        else:
            print('Wrong. The capital of ' + province + ' is ' + chinese_capitals[province] + '.')
            incorrect += 1

    print('Number of correct answers:', correct)
    print('Number of wrong answers:', incorrect)
    

main()

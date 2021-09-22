import random

def main():
    f = open('codes.txt', 'r')

    d={}
    for line in f:
        l = line.split(' ')
        d[l[0]] = l[1].rstrip()

    f.close()

    print(d)
    
    f = open('chinese-provincial-capitals.txt', 'r')
    content = f.read()
    f.close()

    new_content = ''

    for c in content:
        new_content += d.get(c, c)

    f = open('encrypted.txt', 'w')
    f.write(new_content)
    f.close()

    new_d = {}
    for k, v in d.items():
        new_d[v] = k

    f = open('encrypted.txt', 'r')
    content = f.read()
    f.close()

    new_content = ''

    for c in content:
        new_content += new_d.get(c, c)

    f = open('decrypted.txt', 'w')
    f.write(new_content)
    f.close()


main()

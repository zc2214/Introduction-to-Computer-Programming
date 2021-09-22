def main():
    f = open('codes.txt', 'r')

    codes = {}
    for s in f:
        s = s.rstrip('\n')
        l = s.split(' ')
        codes[l[0]] = l[1]

    f.close()

    fr = open('chinese-provincial-capitals.txt', 'r')
    content = fr.read()
    fr.close()
    
    fw = open('encrypted.txt', 'w')
    for c in content:
        if c.isalpha():
            fw.write(codes[c])
        else:
            fw.write(c)

    fw.close()

    
    


main()

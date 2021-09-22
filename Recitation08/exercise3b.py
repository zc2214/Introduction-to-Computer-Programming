def main():
    f = open('codes.txt', 'r')

    codes = {}
    for s in f:
        s = s.rstrip('\n')
        l = s.split(' ')
        codes[l[1]] = l[0]

    f.close()

    fr = open('encrypted.txt', 'r')
    content = fr.read()
    fr.close()

    list_of_keys = codes.keys()
    
    fw = open('decrypted.txt', 'w')
    for c in content:
        if c in list_of_keys:
            fw.write(codes[c])
        else:
            fw.write(c)

    fw.close()


main()

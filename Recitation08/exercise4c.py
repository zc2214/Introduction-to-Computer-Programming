def main():
    f = open('some_text.txt', 'r')
    content = f.read().lower()
    f.close()

    special_c = '.,;:?!()'

    for c in special_c:
        content = content.replace(c, '')

    content = content.replace('\n', ' ')

    l = content.split()

    s = set(l)

    for word in s:
        print(word)
    


main()

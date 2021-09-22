def main():
    f = open("some_text.txt", 'r')
    s = f.read().lower()
    f.close()

    l = s.split()

    for i in range(len(l)):
        l[i] = l[i].strip("""()!,"';.?""")

    unique_words = set(l)

    for word in unique_words:
        print(word)

main()

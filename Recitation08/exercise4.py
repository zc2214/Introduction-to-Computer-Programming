def main():
    #file with some text generated from randomtextgenerator.com
    f = open('some_text.txt', 'r')
    content = f.read()
    f.close()

    #turn everything in lowercase
    content = content.lower()
    
    special_chars = """,;:.!?'"&()-"""
    #replace special chars by space
    for c in special_chars:
        content = content.replace(c, ' ')

    #split with every whitespace  
    l = content.split()

    unique_words = set(l)

    print(unique_words)

main()

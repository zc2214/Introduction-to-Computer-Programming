#main program
def main():
    a = int(input('Enter an integer: '))
    b = int(input('Enter another integer: '))
    print('\nThe greater value is:',max(a,b))

#def functions
def max(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2

#program
main()

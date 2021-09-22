#main program
def main():
    for t in range(1,11):
        d = falling_distance(t)
        print(t,'seconds -',d,'meters')

#def functions
def falling_distance(time):
    g = 9.81

    d = 0.5 * g * (time ** 2)
    return d

main()

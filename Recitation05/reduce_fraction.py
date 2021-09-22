# Reduce a fraction to its lowest term

def greatest_common_divisor(n, m):
    d = min(n, m)

    while n % d != 0  or m % d != 0:
        d -= 1
    return d

def reduce_fraction(num, den):
    if num == 0:
        return 0, 1

    g = greatest_common_divisor(num, den)

    return num//g, den//g

def main():
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    n, d = reduce_fraction(num, den)
    print("This fraction {0}/{1} can be reduced to {2}/{3}.".format(num, den, n, d))
    
main()

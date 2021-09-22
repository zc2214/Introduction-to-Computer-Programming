def main():
    value = int(input('Enter Property Value: '))
    computePropertyTax(value)


def computePropertyTax(p_value):
    assess = 0.6 * p_value
    tax = (assess // 100) * 0.72
    print(assess, tax)


main()

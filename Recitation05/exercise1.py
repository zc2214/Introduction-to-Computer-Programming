#main program
def main():
    value = int(input('Enter the value of the property:\n> '))
    computePropertyTax(value)


#function def
def computePropertyTax(property_value):
    assessment_value = 0.6 * property_value
    property_tax = 0.72 * (assessment_value // 100);

    print('Assessment value: $' + '%1.2f'%assessment_value)
    print('Property tax: $' + '%1.2f'% property_tax)


#program
main()


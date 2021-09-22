age = int(input("Enter a person's age?\n> "))

if age<=1:
    print('He or she is an infant')
elif age<13:
    print('He or she is a child')
elif age<20:
    print('He or she is a teenager')
else:
    print('He or she is an adult')

organisms = int(input('Starting number of organisms?\n> '))
daily_inc = int(input('Average daily increase (in %)?\n> '))
total_days = int(input('Number of days to multiply?\n> '))

#header print
print('Day\tApproximate Population')

for day in range(total_days):
    print(' ' + str(day) + '\t\t ' + str(organisms))

    #better print
    #print(' ' + str(day) + '\t\t ' + '%g' % organisms)

    organisms *= 1 + daily_inc / 100


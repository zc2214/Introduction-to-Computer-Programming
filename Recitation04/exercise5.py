year = 1    #sentinel variable starting first year

tuition = 8000

while year <= 5:
    print('Year ' + str(year) + ' - First semester: $' + str(tuition))
    print('Year ' + str(year) + ' - Second semester: $' + str(tuition))

    #in order to correct display value
    #print('Year ' + str(year) + ' - First semester: $' + '%1.2f' % tuition)
    #print('Year ' + str(year) + ' - Second semester: $' + '%1.2f' % tuition)
    
    tuition *= 1.03
    year +=1

speed = int(input('What is the speed of the vehicle in kph?\n> '))

total_hours = int(input('How many hours has it traveled?\n> '))

hour = 1        #sentinel variable to keep track of hours elapsed

#header print
print('Hour\tDistance traveled')

#repeat code until we reach the final number of hours
while hour <= total_hours:
    distance = speed*hour
    print('',hour,'\t\t',distance)
    hour += 1

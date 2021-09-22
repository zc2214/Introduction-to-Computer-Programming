speed = float(input('Enter the speed: '))
total_t = int(input('Enter the number of hours: '))

t = 1     # sentinel variable

print('Hour\tDistance Traveled')    #Header line

while t <= total_t:
    print(t, '\t\t', speed * t)
    t += 1

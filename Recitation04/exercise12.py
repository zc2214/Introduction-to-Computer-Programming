import random       #import random module

ones, twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0, 0

for i in range(1000):
    roll = random.randint(1,6)

    if roll == 1:
        ones += 1
    elif roll == 2:
        twos += 1
    elif roll == 3:
        threes += 1
    elif roll == 4:
        fours += 1
    elif roll == 5:
        fives += 1
    else:       #meaning roll == 6
        sixes += 1

print("ones\t", ones)
print("twos\t", twos)
print("threes\t", threes)
print("fours\t", fours)
print("fives\t", fives)
print("sixes\t", sixes)
print("TOTAL\t", ones + twos + threes + fours + fives + sixes)

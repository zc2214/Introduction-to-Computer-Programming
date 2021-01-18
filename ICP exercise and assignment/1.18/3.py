import random
maxnum = 0
for i in range(0,100):
    maxnum=max(maxnum, random.randint(1,100))
print(maxnum)

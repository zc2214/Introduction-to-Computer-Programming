import random
num = int(input("pls enter an int"))
loop = True
list = []
while loop:
    i = random.randint(1,100)
    list = list +[i]
    if len(list) == num:
        loop = False
print(list)
list.sort()
print(list)
odd_list = []
for j in list:
    if j%2 != 0:
        odd_list = odd_list + [j]
print(odd_list)

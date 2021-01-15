mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
j = int(input("pls enter an int"))
list = []
for i in mat:
    k = i[j]
    list = list + [k]
print(list)

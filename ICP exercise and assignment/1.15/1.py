a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
num = int(input("pls enter an int"))
inner_list = a[num]
sum = 0
for i in inner_list:
    sum = sum +i
print(sum)

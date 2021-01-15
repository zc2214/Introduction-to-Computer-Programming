columns = int(input("pls enter num of columns"))
rows = int(input("pls enter num of rows"))
b_list = []
for i in range(1,rows+1):
    small_list = []
    for j in range((i-1)*columns+1,i*columns+1):
        small_list += [j]
    b_list += [small_list]
print(b_list)

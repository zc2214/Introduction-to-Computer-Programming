mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
new_columns = len(mat)
new_rows = len(mat[0])
final_list = []
for j in range(0,new_rows):
    temp_list = []
    for i in mat:
        temp_list += [i[j]]
    final_list += [temp_list]
print(final_list)

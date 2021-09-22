def main():
    square = [[4,9,2],[3,5,7],[8,1,6]]

    for i in range(3):
        for j in range(3):
            print(square[i][j],end=' ')
        print()


    if is_lo_shu_magic_square(square) == True:
        print('It is a Lo Shu Magic Square')
    else:
        print('It is not a Lo Shu Magic Square')
    

def is_lo_shu_magic_square(list):
    #first test on numbers
    for num in range(1,10):  #loop on numbers 1 to 9
        present = False
        for i in range(3):
            if num in list[i]:
                present = True
                break
        if present == False:
            return False
    
    #second test on row/column total
    for i in range(3):
        total_row = 0
        total_column = 0
        
        for j in range(3):
            total_row += list[i][j]
            total_column += list[j][i]

        if total_row != 15:
            return False
        if total_column != 15:
            return False

    #third test on the diagonals
    total_diagonal1 = 0
    total_diagonal2 = 0
    for i in range(3):
        total_diagonal1 += list[i][i]
        total_diagonal2 += list[i][2 - i]

    if total_diagonal1 != 15:
        return False
    if total_diagonal2 != 15:
        return False

    #otherwise
    return True
#Call main
main()

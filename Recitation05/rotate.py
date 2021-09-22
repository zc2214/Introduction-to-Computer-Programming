def main():
    string = input("Enter a string: ")
    shift = int(input("Enter an integer: "))
    print(rotate(string, shift))

def rotate(st,n):
    ans = ''
    for i in st:
        if i == ' ':
            ans += i
        else :
            ans += chr((ord(i) - 97 + n) % 26 + 97) 
    return ans

main()

# string = "zw pfli tfuv nfibj tfiivtkcp pfl jyflcu sv rscv kf ivru kyzj"
# shift = -17

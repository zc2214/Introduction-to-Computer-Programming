file = open("testscores.txt","r")
L = file.read().split("\n")
name = L[0]
s1 = int(L[1])
s2 = int(L[2])
s3 = int(L[3])
avg = (s1+s2+s3)/3
print(name,"average score is:", avg)

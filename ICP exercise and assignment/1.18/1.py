try:
    file1 = open("file1.txt","r")
    file2 = open("file2.txt","r")
    names = file1.read().split()
    numbers = file2.read().split()
    dic = {}
    for i in range(0,len(names)):
        name = names[i]
        number = numbers[i]
        dic[name] = number
        file1.close()
        file2.close()
    print(dic)
except:
    print("input valid file")

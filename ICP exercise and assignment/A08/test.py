def build_attraction_dict():
    # write your code here for Task 1
    file = open("top tourist attractions.txt","r")
    list = file.read().split("\n")
    dic = {}
    for i in list:
        middle = i.find(",")
        key = i[0:middle]
        value = i[middle+1:]
        dic[key] = value
    print(dic)

build_attraction_dict()

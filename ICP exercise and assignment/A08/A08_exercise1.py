# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def build_attraction_dict(filename):
    # write your code here for Task 1
    try:
        file = open(filename,"r")
    except:
        print(err)
    else:
        list = file.read().split("\n")
        attraction_dict = {}
        for i in list:
            middle = i.find(",")
            value = i[0:middle]
            key = i[middle+1:]
            attraction_dict[key] = value
        return attraction_dict

def add_attraction(attraction_dict):
    # write your code here for Task 2
    value = input("pls enter a province")
    key = input("pls enter an attraction name")
    attraction_dict[key] = value
    return attraction_dict
    

def build_province_attraction_dict(attraction_dict):
    # write your code here for Task 3
    province_attraction_dict = {}
    new_values = attraction_dict.keys()
    for i in new_values:
        new_key = attraction_dict[i]
        new_value = i
        province_attraction_dict[new_key] = new_value
        return province_attraction_dict

def most_attractions(province_attraction_dict):
    # write your code here for Task 4
    province_set = set()
    for i in province_attraction_dict.keys():
        if len(province_attraction_dict[i]) >= 3:
            province_set.add(i)
    return province_set

def main():
    # write your code here for Task 5
    attraction_dict = build_attraction_dict('top tourist attractions.txt')
    add_attraction(attraction_dict)
    province_attraction_dict = build_province_attraction_dict(attraction_dict)
    ans_set = most_attractions(province_attraction_dict)
    # print(ans_set)
    print()
    print('Provinces with at least 3 attractions:')
    for province in ans_set:
        print(province)

##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()

'''
Created on Sun Dec 29 17:14:09 2019

@author: hl3797
'''
# PROGRAMMING ASSIGNMENT 08
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def build_attraction_dict(filename):
    # write your code here for Task 1
    try:
        # Initialize dict and read data
        attraction_dict = {}
        data = open(filename, 'r').read().split('\n')
        # print(data)
        for item in data:
            if ',' in item:
                t = item.split(',')
                # Add data to dict
                attraction_dict[t[1]] = t[0]
        # print(attraction_dict)
        return attraction_dict
    except Exception as err:
        print(err)

def add_attraction(attraction_dict):
    # write your code here for Task 2
    attraction_name = input('Input a new attraction: ')
    attraction_province = input('Input the province: ')
    attraction_dict[attraction_name] = attraction_province

def build_province_attraction_dict(attraction_dict):
    # write your code here for Task 3
    province_attraction_dict = {}
    # Convert dict to list [(attr1, prov1), (attr2, prov2), ...]
    attraction_ls = list(attraction_dict.items())
    # print(attraction_ls)
    for item in attraction_ls:
        # Create new dict - dict[province] = [attr1, attr2, ...] + [new attr]
        province_attraction_dict[item[1]] = province_attraction_dict.get(item[1], []) + [item[0]]
    # print(province_attraction_dict)
    return province_attraction_dict

def most_attractions(province_attraction_dict):
    # write your code here for Task 4
    province_set = set()
    for province in province_attraction_dict.keys():
        if len(province_attraction_dict[province]) >= 3:
            province_set.add(province)
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

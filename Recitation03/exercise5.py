import math

num_people = int(input('Enter the number of people attending the cookout: '))
num_hotdog_per_person = int(input('How many hot dogs per person? '))

print()     #blank line

total_hotdog = num_people * num_hotdog_per_person

num_pack_hotdog = math.ceil(total_hotdog / 10)
print('Minimum number of packages of hot dogs: ',num_pack_hotdog)

num_pack_bun = math.ceil(total_hotdog / 8)
print('Minimum number of packages of buns: ',num_pack_bun)

left_hotdog = 10 * num_pack_hotdog - total_hotdog
print('Number of left over hot dogs: ',left_hotdog)

left_bun = 8 * num_pack_bun - total_hotdog
print('Number of left over buns: ',left_bun)

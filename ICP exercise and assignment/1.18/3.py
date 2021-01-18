import random
old_number = 0
for i in range(0,100):
    new_number = random.randint(1,100)
    if new_number > old_number:
        old_number = new_number
print(old_number)

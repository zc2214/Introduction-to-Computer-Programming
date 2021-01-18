string = "Examples of contractions include: don’t, isn’t, and wouldn’t."
list = string.split(" ")
new_list = []
for i in list:
    if not ord("a") <= ord(i[len(i)-1]) <= ord("z"):
        i = i.replace(i[len(i)-1],"")
        new_list = new_list + [i]
    else:
        new_list = new_list + [i]
print(new_list)

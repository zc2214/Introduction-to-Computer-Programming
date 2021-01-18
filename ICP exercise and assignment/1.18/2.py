dic = {"simon":"Daniel","Simon":"daniel"}
first_names = dic.copy().keys()
for i in first_names:
    if not ord("A") <= ord(i[0]) <= ord("Z"):
        dic.pop(i)
print(dic)

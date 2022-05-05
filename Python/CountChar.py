name = input()
st = set(name)
dict = {}
for i in st:
    dict[i] = name.count(i)
print(dict)
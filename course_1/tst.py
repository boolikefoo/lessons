list1 = "1, 2, 3, 4, 5"
list2 = "123, 234, 456"
d = {1:["123123"]}
if 1 in d.keys():
    d[1].append("123")
else:
    d[1] = "321"

print(d[1])
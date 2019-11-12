n = int(input())
i = 0
orph = []
text = []
many = set()
while i < n:
    orph.append(input().lower())
    i += 1
i = 0
n = int(input())
while i < n:
    text.extend(input().split(" "))
    i += 1

for i in text:
    if orph.count(i.lower()) > 0:
        pass
    else:
        many.add(i)
print(*many, sep="\n")


    
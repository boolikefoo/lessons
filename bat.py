s = ""

with open("bat.txt", "r", encoding="utf-8") as inf:
    for line in inf:
        s += line

print(s)     
#s = "abc a bCd bC AbC BC BCD bcd ABC"
ls = ''
with open("dataset_3363_3.txt", "r") as inf:
    for line in inf:
        ls += line.strip('\n') + ' '

lsl = ls.lower().split(' ')
mx = 0
pr = ''
for i in lsl:
    if lsl.count(i) > mx:
        mx = lsl.count(i)
        pr = i

print(pr, mx)
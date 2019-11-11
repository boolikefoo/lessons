# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
myd = {}
cnt = 0
'''
for x in range(n):
    s = int(input())
    print(myd.get(s, f(s)))
    myd = {s:f(s)}
'''

while cnt < n:
    s = int(input())
    if s in myd:
        print(myd[s])
    else:
        myd = {s:f(s)}
        print(myd[s])
    cnt += 1
    



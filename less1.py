def decode_file(s):
    
    i = 0
    ns = ''
    ch = ''
    cnum = ''
    while i < len(s):
        if s[i].isalpha():
            ns += s[i]
        elif s[i].isdigit:
            cnum += s[i]
            if s[i+1].isalnum and s[i] < len(s):
                cnum += s[i]
            else:
                pass

    with open("data2.txt", "w") as ouf:
        ouf.write(str('new some text'))
    return ns    

with open("data.txt", "r") as inf:  #читаем строку
    s = inf.readline()

decode_file(s)
print(decode_file(s))    
alpha = input()
salt = input()
for_code = input()
for_decode = input()
la = [i for i in alpha]
ls = [i for i in salt]

def coder(st, fn, alp = la, slt = ls):

    codict = {key:value for key,value in zip(alp,slt)}
    decodict = {key:value for key,value in zip(slt,alp)}
    decoded = ""
 
    for i in range(len(alpha)):     #создаём словарь
        codict[alp[i]] = slt[i]     #Словарь кодировки
        decodict[slt[i]] = alp[i]   #Словарь декодировки
    
    if fn == "code":
        for i in st:
            decoded += codict[i]
    elif fn == "decode":
        for i in st:
            decoded += decodict[i]
    else:
        return 
    return decoded

print(coder(for_code, "code"), coder(for_decode, "decode"), sep='\n')

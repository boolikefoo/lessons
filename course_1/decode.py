def deco(s):
    ns =''
    dig = ''
    lastchar = ''
    for i in range(len(s)):
        if s[i].isalpha() and dig == '':
            #ns += s[i]
            lastchar = s[i]
        elif s[i].isalpha() and dig != '':
            ns += lastchar * int(dig)
            lastchar = s[i]
            dig = ''    
        elif s[i].isdigit():
            if s[i].isdigit() and dig == '':
                dig = s[i]
                
            elif s[i].isdigit() and dig != '':
                dig += s[i]
    if dig != '' and lastchar != '':
        ns += lastchar * int(dig)
        dig = ''
        lastchar = ''


    return ns
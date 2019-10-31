s = "k19p5a14S16o10Z7x16G8X20L2Y7n18x16V1q12j7t16k11V13e11"

print(s.isalnum())
ns = {}
key = ''
bd = 0
lc = ''
for i in s:
    if i.isalpha():
        key = i
        bd = 0

    elif i.isdigit():
        ns[key] = {i}
        bd = 1
        
        if bd != 0:
            lc += i            
            ns.update({key : lc})
           
        else:
            pass
        
   
print(ns)        
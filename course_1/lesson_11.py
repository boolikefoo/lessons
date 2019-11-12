class_list = []
class_dict = {}

with open("dataset_3380_5.txt", "r") as inf:
    for line in inf:
        l = line.strip('\n').split('\t')
        
        if l[0] in class_dict.keys():
            class_dict[l[0]].append(l[2:])
            pass
        else:
            class_dict[l[0]] = [l[2:]]
sm = 0
for i in range(1,12):
    if str(i) in class_dict.keys():    
        for j in class_dict[str(i)]:
            sm += int(j[0])
            #print(i, j)   
        sm = float(sm) / len(class_dict[str(i)])
        print(i, sm )
        sm = 0
        
    else:
        print(i, "-")    



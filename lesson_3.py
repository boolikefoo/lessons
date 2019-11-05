all_dict = {}
md = []
mid = 0
cnt = 0
mid_a_r = 0
mid_a_m = 0
mid_a_f = 0
with open("journal.txt", "r") as inf:
    for line in inf:
        all_dict = line.strip()
        md = all_dict.split(";")
        mid = (float(md[1]) + float(md[2]) + float(md[3])) / 3
        print(mid)

        mid_a_r += float(md[1])
        mid_a_m += float(md[2])
        mid_a_f += float(md[3])
        cnt += 1
        mid = 0

print((mid_a_r / cnt), (mid_a_m / cnt), (mid_a_f / cnt))        

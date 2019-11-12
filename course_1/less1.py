import decode 


s = ''
with open("dataset_3363_2.txt", "r") as inf:  #читаем строку
    s = inf.readline().strip()

ns = decode.deco(s)     #декодируем

with open("out_dataset.txt", "w") as ouf:   #записываем в файл
    ouf.write(ns)

print(ns, s)
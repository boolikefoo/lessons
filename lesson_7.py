a = [[int(i) for i in input().split()]]     #считываем первую строку
b = input()                                 #читаем вторую строку
while b != 'end' :                          #заходим в цикл и читаем данные пока не введут end
    a.append([int(i) for i in b.split()])   #добавляем введённое значение в конец списка a
    b = input()                             #считываем новое значение

for i in a:
    for j in i:
        print(j)

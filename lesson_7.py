'''
a = [[int(i) for i in input().split()]]     #считываем первую строку
b = input()                                 #читаем вторую строку
while b != 'end' :                          #заходим в цикл и читаем данные пока не введут end
    a.append([int(i) for i in b.split()])   #добавляем введённое значение в конец списка a
    b = input()                             #считываем новое значение
'''

a = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
c = []
for i in range(len(a)):
    for j in range(len(a[i])):
        #c[i][j] += a[i-1][j] + a[(i+1)%len(a)][j] + a[i][j-1] + a[i][(j+1)%len(a)]
        print(a[i-1][j] + a[(i+1)%len(a)][j] + a[i][j-1] + a[i][(j+1)%len(a[i])], end=' ')
    print()    


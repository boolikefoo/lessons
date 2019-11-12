#восток = х, север = y, запад = -x, юг = -y
n = int(input())
x, y, i = 0, 0, 0

coord = ""

while i < n:
    coord = input().split(" ")
    if coord[0] == "восток":
        x += int(coord[1])
    elif coord[0] == "запад":
        x -= int(coord[1]) 
    elif coord[0] == "север":
        y += int(coord[1])
    elif coord[0] == "юг":
        y -= int(coord[1])
    i += 1

print(x, y)


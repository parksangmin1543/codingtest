n = int(input())

array = []
array = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 1, 1
move_type = ['L', 'R', 'U', 'D']
for i in array:
    for j in range(len(move_type)):
        if move_type[j] == i:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)
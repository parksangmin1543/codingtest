n = input()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1
steps = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
result = 0

for step in steps:
    x = row + step[0]
    y = column + step[1]

    if x < 1 or x > 8 or y < 1 or y > 8:
        continue
    result += 1
    
print(result)
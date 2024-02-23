array = [7, 5, 9, 0, 3, 1, 6, 2,9, 1, 4, 8, 0, 5, 2, 15]
#인덱싱 과정을 거친다면 좋지않을까?
count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')
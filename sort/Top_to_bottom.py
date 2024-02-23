n = int(input())

array = []
#배열 함수에대해 공부하기
for i in range(n):
	array.append(int(input()))

array.sort(reverse=True)

for i in array:
	print(i, end=' ')
# print(array)

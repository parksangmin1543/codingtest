# 이진탐색
""" def binary_search_Recursive(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2

	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)

def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid - 1
		elif array[mid] < target:
			start = mid + 1
	return None
n, target =list(map(int, input().split()))

array = list(map(int, input().split()))

# result = binary_search_Recursive(array, target, 0, n - 1)
result = binary_search(array, target, 0, n - 1)
if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1) """

# 계수 정렬
""" n = int(input())
array = [0] * 100001

for i in input().split():
	array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
	if array[i] == 1:
		print('yes', end=' ')
	else:
		print('no', end=' ') """

# 집합 자료형
n = int(input())

array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
	if i in array:
		print('yes', end=' ')
	else:
		print('no', end=' ')


def binary_search(array, target, start, end):
	if start > end:
		return None
	
	mid = (start + end) // 2

	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in b:
	if (binary_search(a, i, 0, n - 1) != None):
		print('yes', end=' ')
	else:
		print('no', end=' ')



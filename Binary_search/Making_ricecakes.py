def binary_search(array, target, start, end):
	total = 0
	mid = (start + end) // 2
	for i in array:
		if i > mid:
			total += i - mid
	if start > end:
		return mid
	if target == total:
		return mid
	elif total < target:
		return binary_search(array, target, start, mid - 1)
	else:
		return binary_search(array, target, mid + 1, end)
	
n, m = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array, m, 0, max(array)))




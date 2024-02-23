"""
N개의 원소 K번 바뀌치기
A의 원소의 합이 최대가 되도록
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(len(a)):
	if k == 0:
		break
	# for j in range(len(a) - i)
	if a[i] < b[i]:
		a[i], b[i] = b[i], a[i]
		k -= 1

print(sum(a))

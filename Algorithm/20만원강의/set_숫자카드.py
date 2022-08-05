n = int(input())
ans = list(map(int, input().split()))
m = int(input())
que = list(map(int, input().split()))
A = []
a = 0
for q in range(len(que)):
	for a1 in ans:
		if que[q] == a1:
			a += 1
	if a  == 0:
		A.append(0)
	else:
		A.append(a)
		a = 0

for a in A:
	print(a, end=" ")
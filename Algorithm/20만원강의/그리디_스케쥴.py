## 가장 빨리 끝나고 겹치면 그중에 가장 회의 시간이 짧은애
n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
L = sorted(L, key = lambda x: x[1])
ans = 0
## 처음 고른애의 끝나는 시간
key= 0
for l in L:
	if l[0] < key:
		continue
	else:
		key = l[1]
		ans += 1
print(ans)
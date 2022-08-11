from collections import deque
n,m = map(int,input().split())
g = list(map(int,input().split()))
## 오름차순
g = sorted(g)
## 내림차순
## 최대한 두명이서 타는 횟수를 올리면됨
s = 0
k = 0
vis =[True] * n
for i in range(n-1,0,-1):
	if g[i] + g[k] <= m and vis[i] == True and vis[k]== True and i != k:
		s += 1
		vis[i] = False
		vis[k] = False
		k += 1

print(n-s)
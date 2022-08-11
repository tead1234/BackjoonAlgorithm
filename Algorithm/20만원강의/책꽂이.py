n,m = map(int,input().split())
L = [int(input()) for _ in range(n)]

key = 0
ans = 0
aList = []
vis = [False] * n
## x개를 골라서 만들수 있는 최소의 값을 탐색
def dfs(s,key,x):
	global ans
	if key == x:
		if ans >= m:
			aList.append(ans -m)
		return
	else:
		## 스타트

		for a in range(len(L)):
			if vis[a] == False:
				vis[a] = True
				ans += L[a]
				dfs(a,key+1,x)
				vis[a] = False
				ans -= L[a]
	return
for i in range(n):
	for j in range(1,n+1):
		vis[i] = True
		ans += L[i]
		key += 1
		dfs(i,0,j)
		ans = 0
		key = 0
		vis = [False] * n
print(min(aList))


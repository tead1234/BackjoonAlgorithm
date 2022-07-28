n = int(input())
r= int(input())
List = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
for _ in range(r):
	s,e = map(int,input().split())
	List[s].append(e)
	List[e].append(s)
List = [list(sorted(set(a))) for a in List]
ans = 0
def	dfs(x):
		global ans
		if visited[x]:
			return
		else:
			visited[x] = True
			ans += 1
			for a in List[x]:
				if visited[a] == False:
					dfs(a)
		return
dfs(1)
print(ans)
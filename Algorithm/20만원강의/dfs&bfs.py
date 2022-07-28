from collections import deque
n,l,start = map(int,input().split())
List = [[] for _ in range(n+1)]
q = deque()
for _ in range(l):
	s,e = map(int,input().split())
	List[s].append(e)
	List[e].append(s)
List = [list(sorted(set(a))) for a in List]
print(List)
visited = [False] * n
visited2 = [False] * n
ans = []
ans2 = []
def dfs(x):
	if visited[x-1] == True:
		return
	elif visited[x-1] == False:
		visited[x-1] = True
		ans.append(x)
		for i in List[x]:
			if visited[i-1] == False:
				dfs(i)
	return

def bfs(x):
	q.append(x)
	ans2.append(x)
	while q:
		X = q.popleft()
		if visited2[X-1] == True:
			continue
		else:
			visited2[X-1] = True
			for a in List[X]:
				if a in q or visited2[a-1] == True:
					continue
				else:
					q.append(a)
					ans2.append(a)
dfs(start)
for a in ans:
	print(a, end=" ")
print("\t")
bfs(start)
for a in ans2:
	print(a, end=" ")
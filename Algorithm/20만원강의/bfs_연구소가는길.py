from collections import deque
n,m = map(int,input().split())
## 인접리스트
List = [[] for _ in range(n+1)]
minVal = 9876
val = []
q = deque()
for _ in range(m):
    a,b,c = map(int,input().split())
    if [b,c] not in List[a]:
        List[a].append([b,c])
    if [a,c] not in List[b]:
        List[b].append([a,c])
## bfs 0부터 해야지 될듯?
visited = [False] * (n+1)
def dfs(x,d):
    global minVal
    if x == n:
        val.append(d)
        return
    else:
        visited[x] = True
        for li in List[x]:
            a,b = li
            if visited[a] == False:
                dfs(a,d+b)
                visited[a] = False
    ## 위의 for 함수를 다 거치고 나면 꺼줘야됨
    return

dfs(1,0)
print(min(val))

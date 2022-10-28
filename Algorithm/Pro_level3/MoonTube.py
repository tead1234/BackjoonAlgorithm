N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a - 1].append([c, b - 1])
    G[b - 1].append([c, a - 1])
vis = [False] * N
path = []
ansList = []
ans = 0
ANSWER = []


## 스타트부터 모든 점들과의 유사도를 다 알 수 있어야 하네

def dfs(start, end, path):
    global ans
    if start == end:
        ans = sorted(path)[0]
        return
    else:
        for k in range(len(G[start])):
            c1, d = G[start][k]
            if vis[d]:
                continue
            vis[d] = True
            path.append(c1)
            dfs(d, end, path)
            path.pop()
            vis[d] = False
# dfs(0,0,path)
# print(ans)

for i in range(N):
    for j in range(N):
        vis[i] = True
        if i == j:
            continue
        dfs(i, j, path)
        path = []
        vis = [False] * N
        ansList.append(ans)
        ans = 0
    ansList.sort()
    ANSWER.append(ansList)
    ansList = []
for _ in range(Q):
    an = 0
    k, v = map(int, input().split())
    for val in ANSWER[v - 1]:
        if val >= k:
            an += 1
    print(an)

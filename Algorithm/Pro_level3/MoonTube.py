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

def dfs(start, end, path,vis):
    global ans
    if start == end:
        ans = sorted(path)[0]
        return
    else:
        for k in range(len(G[start])):
            c1, d = G[start][k]

            if vis[d]:
                continue
            else:
                vis[d] = True
                path.append(c1)
                dfs(d, end, path,vis)
                path.pop()
                vis[d] = False


for i in range(N):
    for j in range(N):
        vis[i] = True
        if i == j:
            continue
        dfs(i, j, path,vis)
        # print(vis)
        path = []
        vis = [False] * N
        ansList.append(ans)
        ans = 0
    ANSWER.append(ansList)
    ansList = []
for _ in range(Q):
    an = 0
    k, v = map(int, input().split())
    for val in ANSWER[v - 1]:
        if val >= k:
            an += 1
    print(an)

## bfs 가지치기 >>
import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())

# make weighted graph
G = {n: deque() for n in range(1, N + 1)}
for _ in range(N - 1):
    p, q, v = map(int, sys.stdin.readline().split())
    G[p].append((q, v))
    G[q].append((p, v))

for _ in range(Q):
    ki, vi = map(int, sys.stdin.readline().split())
    visited, queue, ans = [0] * (N + 1), deque(), 0

    # BFS
    visited[vi] = 1
    for v, k in G[vi]:
        visited[v] = 1
        queue.append((v, k))

    while queue:
        v, k = queue.popleft()

        if k >= ki:
            ans += 1
            for nv, nk in G[v]:
                if not visited[nv]:
                    visited[nv] = 1
                    queue.append((nv, min(k, nk)))

    print(ans)
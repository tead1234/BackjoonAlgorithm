## 일반 bfs돌리면 정점순서대로 움직이니깐 최소거리가 안나올 가능성이 있음
import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
q = []
vis = [False] * (n + 1)
dist = [987654321] * (n + 1)
ans = 0
List = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    List[a].append((c, b))
    List[b].append((c, a))

애미 뒤진

def bfs(x):
    q.append((0, 1))
    heapq.heapify(q)
    dist[1] = 0
    while q:
        a, b = heapq.heappop(q)
        if vis[b]:
            continue
        else:
            vis[b] = True
            for i in List[b]:
                c, d = i
                if vis[d] == False and dist[d] > c + dist[b]:
                    heapq.heappush(q,(c+dist[b],d))
                    dist[d] = dist[b] + c

bfs(1)
print(dist)
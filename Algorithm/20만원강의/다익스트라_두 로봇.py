import heapq
from collections import deque
## 최소 거리가 나오려면 로봇을 한대씩 움직이는데
## 이동거리가 가장 짧은 애부터 먼저 이동 시키고 주변에
# 다른 로봇이 있는지 판단
## 시작에서 목표점까지 가는 경로는 하나이므로
## 그 경로로 가는 거리중 가장 오래걸리는 값을 빼면 답
N,s,g = map(int,input().split())
vis = [False] * (N+1)
길이 = [[] for _ in range(N+1)]
ads = [98746716] * (N+1)
# q = deque()
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,l = map(int,input().split())
    heapq.heappush(g[a], (l,b))
    heapq.heappush(g[b], (l,a))
print(g)
def bfs(start, end):
    vis[start] = False
    q = []
    ads[start] = 0
    # for a in g[start]:
    #     # a는 길이와 다음 방문지들
    #     heapq.heappush(q, a)
    q.append((0,start))
    while q:
        l, visit = heapq.heappop(q)
        if visit == end:
           길이[end].append(l)
           break

        if vis[visit]:
            continue
        else:
            vis[visit] = True
            for b in g[visit]:
                c,d = b
                if vis[d] == False:
                    if ads[d]> ads[visit] + c:
                        heapq.heappush(q,(c+ ads[visit], d))
                        길이[d].append(c)
                        ads[d] = ads[visit] + c

bfs(s,g)
print(ads)
print(길이)
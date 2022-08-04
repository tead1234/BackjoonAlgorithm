import sys
import heapq
n = int(input())
q = []
List = [list(map(int,input())) for _ in range(n)]
vis = [[False] * (n) for _ in range(n)]
dist = [[98765312]  * n for _ in range(n)]

def bfs():
    ## 힌칸으로 가면 거리는 0
    ## 아니면 1
    ## q에 들어가는 값은 거리, x, y
    heapq.heappush(q,(0,0,0))
    dist[0][0] = 0

    while q:
        a,b,c = heapq.heappop(q)
        if vis[b][c]:
            continue
        else:
            vis[b][c] = True
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
            for i in range(4):
                if n > dx[i] + b >=0 and n> dy[i] + c >= 0:
                    if vis[dx[i] + b][dy[i] + c] == False and  List[dx[i] + b][dy[i] + c] == 1:
                        heapq.heappush(q,(dist[b][c] + 0, dx[i] + b, dy[i] + c))
                        dist[dx[i] + b][dy[i] + c] = dist[b][c] + 0
                    elif vis[dx[i] + b][dy[i] + c] == False and  List[dx[i] + b][dy[i] + c] == 0:
                        heapq.heappush(q, (dist[b][c] + 1, dx[i] + b, dy[i] + c))
                        dist[dx[i] + b][dy[i] + c] = dist[b][c] + 1
bfs()
print(dist)

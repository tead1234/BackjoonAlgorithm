from collections import deque
N,M = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(N)]
ans = 0
## 최단거리만 구하는건 다했는데 m개로 제한하는건 어찌할까
def bfs(x,y):
    global ans
    q = deque()
    dist = [[0] * N for _ in range(N)]
    dist[x][y] = 1
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        X,Y = q.popleft()
        ## 다음 큐에 들어갈 수 있는 후보들을 탐색 거리가 1인 경우만
        for i in range(4):
            nx = dx[i] + X
            ny = dy[i] + Y
            if N > ny >=0 and N> nx >= 0:
                if dist[nx][ny] == 0:
                    q.append((nx,ny))
                    dist[nx][ny] = dist[X][Y] + 1
                    if g[nx][ny] == 2:
                        ans += dist[nx][ny] -1
                        return
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            bfs(i,j)
print(ans)



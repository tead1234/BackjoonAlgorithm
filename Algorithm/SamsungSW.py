from collections import deque

queue = deque()
K = int(input())
graph = [list(map(int,input().split())) for i in range(K)]
## 연결 프로세스 갯수
on = 0
## 연결된 전설갯수
link =0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def dfs(x,y,on,link):

    if x>= K or y>= K or x<=-1 or y <= -1:
        return
    if x == K-1 or x ==0 or y ==K-1 or y ==0:
        on += 1
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dx[i] + y
        if graph[nx][ny] ==2:
            return
        if graph[nx][ny] ==0:
            graph[x][y] == 2
            link +=1
            on +=1
            dfs(nx,ny,on, link)








for n in range(K):
    for m in range(K):
        if graph[n][m] ==1:
            queue.append((n,m))

while queue:
    o,p = queue.popleft()
    dfs(o,p,on, link)

    print(on,link)

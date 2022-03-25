from collections import deque
M,N = map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(input()))
queue = deque()
## 오른쪽, 위쪽, 왼쪽, 아래
dx = [0,-1,0,1]
dy = [1,0,-1,0]
answer = 0
## 유망한지 여부 찾기
def check(x,y):
    if graph[x][y]== '.':
        return True
    else:
        return False
def DFS(x,y):
    if graph[x][y] == 'O':
        return
    else:
        for i in range(4):
            X = dx[i] + x
            Y = dy[i] + y
            if check(X,Y):
                DFS(X,Y)


for i in range(M):
    for j in range(N):
        if graph[i][j] == 'R':
            DFS(i,j)


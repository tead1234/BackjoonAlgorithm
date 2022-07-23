from collections import deque
m,n = map(int,input().split())
g= [list(input()) for _ in range(m)]
dis = [[0] * n for _ in range(m)]
q = deque()
def bfs(x,y):
    q.append([x,y])
    dis[x][y] = 1
    while q:
        a,b = q.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for k in range(4):
            A = dx[k] + a
            B = dy[k] + b
            if m>A>=0 and n>B>=0 and g[A][B] != '#' and dis[A][B] == 0 :
                dis[A][B] = dis[a][b] +1
                q.append([A,B])
for i in range(m):
    for j in range(n):
        if g[i][j] == 'A':
            bfs(i,j)
for i in range(m):
    for j in range(n):
        if g[i][j] == 'B':
            if dis[i][j] == 0:
                print('NO')
            elif dis[i][j] != 0:
                print("YES")
                print(dis[i][j] -1)

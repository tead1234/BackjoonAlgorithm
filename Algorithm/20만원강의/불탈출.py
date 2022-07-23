from collections import deque
T =int(input())
q = deque()
q2 = deque()
ans = 0
def Finfire(w,z):
    q2.append((w,z))
    fire[w][z] = 1
    while q2:
        w1, z1 = q2.popleft()
        dw = [-1, 0, 1, 0]
        dz = [0, -1, 0, 1]
        for k in range(4):
            W = dw[k] + w1
            Z = dz[k] + z1
            if g[W][Z] != "#" and n>W>=0 and m>Z>=0 and fire[W][Z] == 0 :
                q2.append((W,Z))
                fire[W][Z] = fire[w1][z1] + 1
            elif W == m - 1 or W == 0 or Z == n - 1 or Z == 0:
                if g[W][Z] != '#' and fire[W][Z] == 0:
                    fire[W][Z] = fire[w1][z1] + 1
                    return
def bfs(start, visited):
    global ans
    q.append(start)
    o,p = start
    visited[o][p] = 0
    while q:
        x,y = q.popleft()
        if x > m or y >m or 0> x or 0>y:
            return
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for k in range(4):
            X = dx[k] + x
            Y = dy[k] + y
            if (X == m-1 and Y ==0) or (X == m-1 and Y ==n-1) or  (X ==0 and Y == n-1) or (X==0 and Y ==0):
                ans = visited[X][Y]
                return
            if g[X][Y] != "#" and fire[X][Y] > visited[X][Y] == 0:
                q.append((X,Y))
                visited[X][Y] = visited[x][y] + 1


for _ in range(T):
    m,n =map(int,input().split())
    g = [list(input()) for _ in range(n)]
    fire = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j1 in range(m):
            if g[i][j1] == '*':
                Finfire(i,j1)
    print(fire)
    for i in range(n):
        for j in range(m):
            if g[i][j] == "@":
                start = (i,j)
                bfs(start,visited)
                print(ans)

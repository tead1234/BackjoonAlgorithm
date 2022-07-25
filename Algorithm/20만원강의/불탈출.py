from collections import deque

T = int(input())
q = deque()
q2 = deque()
ans = -1
fireList = []
def Finfire(fireList):
    for fir in fireList:
        q2.append(fir)
        w, z = fir
        fire[w][z] = 1
    while q2:
        w1, z1 = q2.popleft()
        dw = [-1, 0, 1, 0]
        dz = [0, -1, 0, 1]
        for k in range(4):
            W = dw[k] + w1
            Z = dz[k] + z1
            if n > W >= 0 and m > Z >= 0:
                if g[W][Z] != "#":
                    if fire[W][Z] == 0:
                        q2.append((W, Z))
                        fire[W][Z] = fire[w1][z1] + 1

def bfs(start, visited):
    global ans
    q.append(start)
    o, p = start
    visited[o][p] = 1
    if o == n-1 or p == m-1 or o ==0 or p == 0:
        ans =1
        return
    while q:
        x, y = q.popleft()
        if n > x >= 0 and m > y >= 0:
            if x == n - 1 or x == 0 or y == m - 1 or y == 0:
                if g[x][y] == ".":
                    ans = visited[x][y]
                    return
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for k in range(4):
            X = dx[k] + x
            Y = dy[k] + y
            if n>X>=0 and m>Y>=0 and g[X][Y] == "." and fire[X][Y] > visited[x][y] and visited[X][Y] == 0:
                q.append((X, Y))
                visited[X][Y] = visited[x][y] + 1
for _ in range(T):
    m, n = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    fire = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    fireList = []
    for i in range(n):
        for j1 in range(m):
            if g[i][j1] == '*':
                fireList.append((i, j1))
    Finfire(fireList)
    for i in range(n):
        for j in range(m):
            if g[i][j] == "@":
                start = (i, j)
                bfs(start, visited)
                if ans == -1:
                    print("IMPOSSIBLE")
                else:
                    print(ans)
                    ans = -1

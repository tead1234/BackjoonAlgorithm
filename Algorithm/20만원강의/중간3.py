from collections import deque

n,m = map(int,input().split())
g = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
def bfs(x,y):
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for k in range(4):
            X = dx[k] + x
            Y = dy[k] + y
            if n > X >= 0 and m > Y >= 0 and g[X][Y] != '1' and visited[X][Y] == False:
                q.append((X, Y))
                visited[X][Y] =True
for i in range(m):
    if g[0][i] == '0':
        bfs(0,i)

for j in range(m):
    if True in visited[n-1]:
        print("Yes")
        break
    else:
        print("NO")
        break
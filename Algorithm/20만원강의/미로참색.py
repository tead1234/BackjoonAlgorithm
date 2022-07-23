from collections import deque
a,b = map(int,input().split())
answer = 1
g = [list(map(int,list(input()))) for i in range(a)]
visited = [[0] * b for _ in range(a)]
q = deque()
def bfs(x,y,q):
    if (x,y) not in q:
        q.append((x,y))
        visited[x][y] = 1
    while q:
        if (a-1,b-1) in q:
            return

        elif visited[x][y] != 0 and g[x][y] == 1:
            x,y = q.popleft()
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if a>X>=0 and b>Y>=0 and visited[X][Y] == 0 and visited[x][y] != 0 and g[X][Y] == 1:
                    q.append((X,Y))
                    visited[X][Y] = visited[x][y] + 1

bfs(0,0,q)
if visited[a-1][b-1] == 0:
    print(-1)
print(visited[a-1][b-1])






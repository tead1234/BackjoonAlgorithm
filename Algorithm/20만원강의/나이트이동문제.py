from collections import deque
T = int(input())
q = deque()
ans = 0
def bfs(x,y,w,z,l):
    global ans
    ans = 0
    ## 체스판
    g = [[False] * l for _ in range(l)]
    visited = [[0]* l for _ in range(l)]
    q.append((x,y))
    visited[x][y] = 0
    g[x][y] = True
    while q:
        if (w,z) in q:
            ans = visited[w][z]
            gra = visited
            return
        i,j = q.popleft()
        di = [-2, -1, 1, 2 , -2, -1, 1, 2]
        dj = [-1, -2, -2, -1, 1,2,2,1]
        for k in range(8):
            I = di[k] + i
            J = dj[k] + j
            if l>I>=0 and l> J >=0 and g[I][J] == False and visited[I][J] == 0:
                q.append((I,J))
                visited[I][J] = visited[i][j] + 1

for _ in range(T):
    l =int(input())
    x,y = map(int,input().split())
    w,z = map(int,input().split())
    bfs(x,y,w,z,l)
    print(ans)

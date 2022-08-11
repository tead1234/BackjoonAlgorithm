from collections import deque
n, m = map(int, input().split())
for i in range(n+1):
    for j in range(m+1):
        pass

g = [list(map(int, input().split())) for _ in range(n)]

ans = 0
cnt = 0
q = deque()
flag = False
## 외부 치즈 칠하기
def bfs(x):
    a,b = x
    g[a][b] = 3
    q.append((a,b))
    while q:
        c,d = q.popleft()
        g[c][d] = 3
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        for k in range(4):
            if n> dx[k] + c>=0 and m> dy[k] + d >= 0:
                if g[dx[k] + c][dy[k]+ d] == 0:
                    q.append((dx[k] + c,dy[k]+ d))
bfs((0,0))




def clear():
    global cnt
    global ans
    global flag
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                for k in range(4):
                    if n > dx[k] + i >= 0 and m > dy[k] + j >= 0:
                        if g[dx[k] + i][dy[k] + j] == 3:
                            cnt += 1
                if cnt >= 2:
                    g[i][j] = 2
                    flag = True
                    cnt = 0
    if flag:
        for i in range(n):
            for j in range(m):
                if g[i][j] == 2:
                    g[i][j] = 3
        print(g)
        flag = False
        ans += 1
        clear()
    else:
        return


clear()
print(ans)



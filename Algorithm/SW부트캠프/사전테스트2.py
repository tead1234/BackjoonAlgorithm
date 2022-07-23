a = list(map(int,input().split()))
g = [list(map(int,list(input()))) for i in range(a[0])]
visited = [[False] * a[1] for i in range(a[0])]
answer = 0
def dfs(x,y,g):
    global answer
    if a[0]>x>=0 and a[1] > y >= 0:
    # 위 왼쪽, 아래, 오른쪽
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        if visited[x][y] == False:
            if g[x][y] == 1:
                visited[x][y] = True
                answer += 1
                for i in range(4):
                    X = dx[i] + x
                    Y = dy[i] + y
                    if vaild(X,Y,g, visited):
                        dfs(X,Y,g)
    return
def vaild(x,y, g , visited):
    ## 사방에 막힌곳이 없어야함 >> 주변에 1이 무조건 있고 거긴 False여야함
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        X = dx[i] + x
        Y = dy[i] + y
        if a[0]> X >= 0 and a[1] > Y >=0:
            if g[X][Y] == 1 and visited[X][Y] == False:
                return True
    return False
dfs(0,0,g)
print(visited)
print(answer)
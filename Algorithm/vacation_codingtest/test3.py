li = list(map(int,input().split()))
g = [list(input()) for _ in range(li[0])]
answer = 0
def bfs(i,j,g):
    if g[i][j] == '.' and g[i][j] != True:
        g[i][j] = True
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        for k in range(4):
            X = dx[k] + i
            Y = dy[k] + j
            if li[0] > X >= 0 and li[1] > Y >= 0 and g[X][Y] != '#':
                bfs(X,Y,g)

    return
for i in range(li[0]):
    for j in range(li[1]):
        if g[i][j] == '.':
            bfs(i,j,g)
            answer += 1
print(answer)

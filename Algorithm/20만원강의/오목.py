g = [list(input()) for _ in range(7)]
sum_ = 0
ans = 0
## 대각선 상하, 좌우
def dfs(g,i,j, dx, dy):
    global sum_
    if 7> dx + i >=0 and 7> dy+j>=0:
        m = g[i][j]
        if sum_ == 5:
            sum_ = 0
            return True
        if g[i+dx][j+dy] == m:
            sum_ += 1
            dfs(g,i+dx,j+dy, dx,dy)
    return False


for i in range(7):
    for j in range(7):
        if g[i][j] == 'O' or g[i][j] ==  'X':
            ## 상, 왼, 아,오, 좌아, 우아, 좌상, 우상
            for k in range(8):
                dx = [-1,0,1,0,1,1,-1,-1]
                dy = [0,-1,0,1, -1,1,-1,1]
                if 7 > (i + dx[k])>= 0 and 7 > (j+ dy[k]) >= 0:
                    if dfs(g,i,j, dx[k], dy[k]):
                        print(g[i][j])


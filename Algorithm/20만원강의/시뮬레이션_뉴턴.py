n,m = map(int,input().split())
g = [list(input()) for _ in range(n)]
## 아래부터 떨구기
def downTo(X):
    a,b = X
    if n>a+1>=0:
        if g[a+1][b] == ".":
            g[a+1][b] = "o"
            g[a][b] = '.'
            downTo((a+1,b))
        elif g[a+1][b] == '#':
            return
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if g[i][j] == 'o':
            downTo((i,j))
for a in range(n):
    for b in range(m):
        print(g[a][b], end="")
    print('')
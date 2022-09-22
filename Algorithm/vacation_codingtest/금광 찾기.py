T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    G = list(map(int,input().split()))
    G2 = []
    for i in range(0,len(G),4):
        G2.append(G[i:i+m])

    ANS = []
    ansList = []
    visted = [[0]* m for _ in range(n)]
    ## 시작 점을 넣어서 나올 수 있는 모든 경우를 다 찾아서
    dx = [-1,0,1]
    dy = [1,1,1]
    ans = 0
    def dfs(x,y):
        global ans
        visted[x][y] = 1
        ans += G2[x][y]
        ## 3가지 방향을 탐색
        for k in range(3):
            X = dx[k] + x
            Y = dy[k] + y
            if n > X >=0 and m > Y >=0:
                ## 방향이 가능하다면
                if visted[X][Y] != 1:
                    dfs(X,Y)
                ANS.append(ans)
                ans -= G2[X][Y]
                visted[X][Y] = 0
    for i in range(3):
        dfs(i,0)
        ansList.append(max(ANS))
        ANS = []
        ans =0

    print(max(ansList))
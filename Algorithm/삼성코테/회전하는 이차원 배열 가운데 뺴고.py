from collections import deque
## 2차원 배열 시계방향 회전
## G라는 원본 배열을 놓고
## G를 카피해놓은 애를 가지고
## GC를 구역마다 돌린다음 복사
G = [
     [1,2,3,4,1],
     [1,1,2,4,4],
     [1,2,2,4,1],
     [3,1,4,4,2],
     [3,1,4,4,1]
     ]
## 시작점과 크기만은 가지고
def rotate(a,b, k):
    # GCOPY
    global G
    G_COPY = []
    ## 애는 일부를 잘라온거고
    for r in range(a,a+k):
        G_COPY.append(G[r][b:b+k])
    mx = k
    GC = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            GC[mx-j-1][i] = G_COPY[i][j]

    for i in range(k):
        for j in range(k):
            G[i+a][j+b] = GC[i][j]
def rotateCross(List,k):
    # l 안에 기존 좌표 랑 값을 가져옴
    save   = []
    for l in List:
        x,y,v = l
        X = y
        Y = k-x-1

        save.append((X,Y,v))
    return save
def score(i,j,n,visi):
    # n 은 대상 숫자
    if visi[i][j] == True:
        return
    q = deque()
    visi[i][j] = True
    q.append((i,j))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while q:
        i, j = q.popleft()
        visi[i][j] = True
        for k in range(4):
            X = i + dx[k]
            Y = j + dy[k]
            if len(G) > X >= 0 and len(G) > Y >= 0:
                ## 색이 같으면 그냥 탐색하면되고
                if G[X][Y] == n and visi[X][Y] == False:
                    q.append((X,Y))
                    # print(X,Y)
                elif G[X][Y] != n and visi[X][Y] == False:
                    dic[G[X][Y]] += 1
                    visi[X][Y] = True
for _ in range(4):
# 돌려야할 꼭지점
    ans = 0
    k = len(G)//2
    dot = [(0,0),(k+1,0), (k+1,k+1), (0,k+1)]
    for d in dot:
        x,y = d
        rotate(x,y,k)
    pre = []
    for i in range(len(G)):
        for j in range(len(G)):
            if i == k:
                pre.append((i,j,G[i][j]))
            if j == k :
                pre.append((i,j,G[i][j]))
    pre = rotateCross(pre,len(G))
    while pre:
        x,y,v = pre.pop()
        G[x][y] =v
    # for g in G:
    #     print(g)
    visi = [[False] * len(G) for _ in range(len(G))]
    dic = {}
    for i in range(1,5):
        dic[i] = 0
    ## 1을 기준으로 돌렸을때
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 1:
                score(i,j,1,visi)
    # 딕셔너리를 가지고 점수계산을 해야
    for k in dic.items():
        a,b = k
        ans += (a*b)
    visi = [[False] * len(G) for _ in range(len(G))]
    dic = {}
    for i in range(1, 5):
        dic[i] = 0
    ## 1을 기준으로 돌렸을때
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 2:
                score(i, j, 2, visi)
    # 딕셔너리를 가지고 점수계산을 해야
    for k in dic.items():
        a, b = k
        ans += (a * b)
    visi = [[False] * len(G) for _ in range(len(G))]
    dic = {}
    for i in range(1, 5):
        dic[i] = 0
    ## 1을 기준으로 돌렸을때
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 3:
                score(i, j, 3, visi)
    # 딕셔너리를 가지고 점수계산을 해야
    for k in dic.items():
        a, b = k
        ans += (a * b)
    visi = [[False] * len(G) for _ in range(len(G))]
    dic = {}
    for i in range(1, 5):
        dic[i] = 0
    ## 1을 기준으로 돌렸을때
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 4:
                score(i, j, 4, visi)
    # 딕셔너리를 가지고 점수계산을 해야
    for k in dic.items():
        a, b = k
        ans += (a * b)
    print(ans)
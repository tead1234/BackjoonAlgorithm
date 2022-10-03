
# 오 위 왼 아
# k는 방향의 크기를 몇번 실행할지 알려주는 키
# cnt는 함수 실행 수 카운터 얘가 2가 되면 k += 1
# graph

# 무브란 함수는 움직일 크기와 방향, 시작점을 넣으면 graph를 칠해줌
def move(start, dir, len, N, G, flag):
    x,y = start
    for _ in range(len):
        X = x + dir[0]
        Y = y + dir[1]
        if N > X>=0 and N > Y >= 0:
            G[X][Y] = 1
            x = X
            y = Y
        else:
            flag = False
            return flag

def init():
    k = 1
    cnt = 0
    N = 7
    G = [[0] * N for _ in range(N)]
    D = [3,0,1,2]
    d = 0
    loc = (2, 2)
    G[loc[0]][loc[1]] = 1
    # 위 왼 아 오
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # 움직이는 순서
    DRE = []
    flag = False
    for i in range(4):
        DRE.append((dx[i], dy[i]))
    x,y = loc
    while not flag:
        for _ in range(k):
            X = x + DRE[D[d]][0]
            Y = y + DRE[D[d]][1]
            if N > X >= 0 and N > Y >= 0:
                G[X][Y] = 1
                x= X
                y = Y
            else:
                flag = True
        for g in G:
            print(g)
        print("")
        d = (d + 1) % 4
        cnt += 1
        if cnt == 2:
            k += 1
            cnt = 0
    

init()
# move(loc,DRE[0],k)


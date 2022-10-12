from collections import deque
N, M = map(int,input().split())
x,y,d = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
# 방향설정 우l 왼 아 오
dx = [-1,0,1,0]
dy = [0,-1,0,1]
# 초기방향부터 설정 첫방향이 0방향이니깐 굳이 설정할 필요 x
Dir = [1,2,3,0]
# 한번 방향 전활 할때마다 + 1
idx = -1
# 예를 들어 첫방향이 오른쪽이면 다음 방향은 위를 봐야 하니
# dir상에선 3번 방향임 > 따라서 한번이동하면 0으로 idx = 2이고
# 왼쪽 탐색
if d == 0:
    idx = 0
elif d == 1:
    idx = 3
elif d == 2:
    idx =2
elif d == 3:
    idx =1
clean = 1
flg = False
def find(x,y,idx):
    # 청소
    global flg
    global clean
    if idx == 0:
        MAP[x][y] = "위"
    elif idx == 1:
        MAP[x][y] = "왼"
    elif idx == 2:
        MAP[x][y] = "아래"
    elif idx == 3:
        MAP[x][y] = "오른쪽"

    for i in MAP:
        print(i)
    print()
    cnt = 0

    for k in range(1,5):
        X= x
        Y = y

        IDX = (idx + k)  % 4
        X += dx[Dir[IDX]]
        Y += dy[Dir[IDX]]
        if N > Y >= 0 and M > X >= 0:
            if MAP[X][Y] == 0:
                clean += 1
                ## 다음 방문을 했는데 다 탐색해도 0이 없을경우
                find(X,Y,IDX)
                if MAP[x + dx[Dir[(IDX + 2)  % 4]]][y + dx[Dir[(IDX + 2)  % 4]]] == 1:
                    flg = True
                    return
        if flg:
            return

find(x,y,idx)

print(clean)
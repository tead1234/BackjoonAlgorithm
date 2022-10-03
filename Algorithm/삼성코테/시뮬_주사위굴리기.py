from collections import deque
N,M,x,y,K = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
updownKey = 3
leftrightKey = 0
# 숫자저장 리스트
color = [0] * 7
# 오른쪽으로 이동 배열
turnRight = deque([3,1,4,6])
# 아래로 회전
turnDown = deque([2,1,5,6])
# order
order = deque(list(map(int,input().split())))
X = x
Y = y
while order:
    ord = order.popleft()
    # print(ord)
    # 4방위 위치 탐색
    if ord == 1:
        Y = y + 1
    elif ord == 2:
        Y = y - 1
    elif ord == 3:
        X = x - 1
    elif ord == 4:
        X = x + 1
    if N > X >=0 and M > Y >= 0:
        x = X
        y = Y
        ## 주사위 이동
        if ord == 1:
            turnRight.append(turnRight.popleft())
            turnDown[1] = turnRight[1]
            turnDown[3] = turnRight[3]
            # 바닥면은 turnRight[3]
            if MAP[X][Y] == 0:
                MAP[X][Y] = color[turnRight[3]]
            elif MAP[X][Y] != 0:
                color[turnRight[3]] = MAP[X][Y]
                MAP[X][Y] = 0
            print(color[turnRight[1]])
        if ord == 2:
            turnRight.appendleft(turnRight.pop())
            turnDown[1] = turnRight[1]
            turnDown[3] = turnRight[3]
            # 바닥면은 turnRight[3]
            if MAP[X][Y] == 0:
                MAP[X][Y] = color[turnRight[3]]
            elif MAP[X][Y] != 0:
                color[turnRight[3]] = MAP[X][Y]
                MAP[X][Y] = 0
            print(color[turnRight[1]])
        if ord == 3:
            turnDown.append(turnDown.popleft())
            turnRight[1] = turnDown[1]
            turnRight[3] = turnDown[3]
            # 바닥면은 turnRight[3]
            if MAP[X][Y] == 0:
                MAP[X][Y] = color[turnDown[3]]
            elif MAP[X][Y] != 0:
                color[turnDown[3]] = MAP[X][Y]
                MAP[X][Y] = 0
            print(color[turnDown[1]])
        if ord == 4:
            turnDown.appendleft(turnDown.pop())
            turnRight[1] = turnDown[1]
            turnRight[3] = turnDown[3]
            # 바닥면은 turnRight[3]
            if MAP[X][Y] == 0:
                MAP[X][Y] = color[turnDown[3]]
            elif MAP[X][Y] != 0:
                color[turnDown[3]] = MAP[X][Y]
                MAP[X][Y] = 0
            print(color[turnDown[1]])
    else:
        X = x
        Y = y
        continue
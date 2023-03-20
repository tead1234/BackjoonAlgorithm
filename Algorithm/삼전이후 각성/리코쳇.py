from collections import deque
import copy
## 포인트는 G를 스쳐지나가는것이 아니라 그 지점에 멈춰야 되는것
## bfs로 돌리다가
## 여기다간 checkMap이 넘어가야될듯
def goaway(x,y, dir_x, dir_y,Map, checkMap):
    a = x
    b = y
    while len(Map) > x + dir_x >= 0 and len(Map[0]) > y + dir_y >= 0 and Map[x + dir_x][y + dir_y] != 'D':
        # if checkMap[x + dir_x][y + dir_y] == '.' or checkMap[x + dir_x][y + dir_y] == 'G':
            # print("check", x,y)
        x = x + dir_x
        y += dir_y
        # else:
        #     break
    if a == x and b == y:
        return checkMap, x,y

    else:
        if str(checkMap[x][y]).isdigit():
            return checkMap, -1, -1
        else:

            checkMap[x][y] = checkMap[a][b] + 1
            return checkMap, x, y
## x, y ㄱ밧을 가져올수 있어야 할거같은데

def play(x,y, Map):
    q = deque()
    checkMap = copy.deepcopy(Map)
    checkMap[x][y] = 0

    # 방향
    des = [(-1,0), (1, 0), (0, -1), (0, 1)]
    q.append((x,y))
    while q:
        a,b = q.popleft()

        for i in range(4):

            checkMap,A, B = goaway(a,b, des[i][0], des[i][1], Map, checkMap)

            if A == a and B == b:
                continue
            elif A == -1 and B == -1:
                continue
            elif Map[A][B] == 'G':
                return checkMap[A][B]
            else:
                q.append((A,B))
    return -1


def solution(board):
    answer = 0
    Board = [list(a) for a in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = play(i,j, Board)
    return answer
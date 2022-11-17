# 각 손가락으로 주어진 숫자를 누를때 걸리는 비용을 계산하고 적게 나온쪽으로 누르고 이동
## 걸리는 비용계산은 bfs 로
from collections import deque


def bfs(a, b):
    q = deque()
    vis = [
        [0] * 3 for _ in range(4)
    ]
    x, y = a
    tar_x, tar_y = b
    if x == tar_x and y == tar_y:
        return 1
    vis[x][y] = 1
    # 가중치
    ans = 0
    q.append((x, y, ans))

    while q:
        i, j, weight = q.popleft()
        ## 제자리 누르기
        if i == tar_x and j == tar_y:
            return weight
        # 상하좌우
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for k in range(4):
            X = dir[k][0] + i
            Y = dir[k][1] + j
            if 4 > X >= 0 and 3 > Y >= 0:
                if vis[X][Y] != 1:
                    q.append((X, Y, weight + 2))
                    vis[X][Y] = 1
        # 대각선
        dir2 = [
            (-1, -1),
            (1, -1),
            (-1, 1),
            (1, 1)
        ]
        for k in range(4):
            X = dir2[k][0] + i
            Y = dir2[k][1] + j
            if 4 > X >= 0 and 3 > Y >= 0:
                if vis[X][Y] != 1:
                    q.append((X, Y, weight + 3))
                    vis[X][Y] = 1
        # print(q)
        # a는 좌표


# print(bfs((0,0),(3,1)))
def solution(numbers):
    answer = 0
    left = (1, 0)
    right = (1, 2)
    for num in numbers:
        if num == '1':
            target = (0, 0)
        elif num == '2':
            target = (0, 1)
        elif num == '3':
            target = (0, 2)
        elif num == '4':
            target = (1, 0)
        elif num == '5':
            target = (1, 1)
        elif num == '6':
            target = (1, 2)
        elif num == '7':
            target = (2, 0)
        elif num == '8':
            target = (2, 1)
        elif num == '9':
            target = (2, 2)
        elif num == '0':
            target = (3, 1)
        elif num == '*':
            target = (3, 0)
        elif num == '#':
            target = (3, 2)
        A = bfs(left, target)
        B = bfs(right, target)
        print("A와 B", A, B, answer)
        if A <= B:
            left = target
            answer += A
        elif B < A:
            right = target
            answer += B
    # max(bfs)
    return answer
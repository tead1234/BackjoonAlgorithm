# from collections import deque
#
# M, N = map(int, input().split())
# graph = []
# for i in range(N):
#     graph.append(list(input()))
# queue = deque()
# ## 오른쪽, 위쪽, 왼쪽, 아래
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
# answer = 0
# ## 백트래킹을 할때마다 +1 을 해주면 해결될거같은데
# ## dfs는 일단 이동하고 판단하는건데
# ## check는 이동할 곳의 미래를 한번더 파악함 즉 dfs를 두번 연속으로 하는 것과 같은효과
# def Right(x,y):
#     if y>=N:
#         return
#     if graph[x][y+1] == '.':
#         graph[x][y]= 1
#         DFS(x,y+1)
#     else:
#         graph[x][y] = 'R'
#         return
# def Left(x,y):
#     if y<0:
#         return
#     if graph[x][y-1] == '.':
#         graph[x][y-1] = 1
#         DFS(x,y)
#     else:
#         graph[x][y] = 'R'
#         return
# def Up(x,y):
#     if x<0:
#         return
#     if graph[x-1][y] == '.':
#         graph[x][y] = 1
#         DFS(x-1,y)
#     else:
#         graph[x][y] = 'R'
#         return
#
# def Down(x,y):
#     if x>=M:
#         return
#     if graph[x+1][y] == '.':
#         graph[x][y] = 1
#         DFS(x+1,y)
#     else:
#         graph[x][y] = 'R'
#         return
# def check(x,y):
#     for i in range(4):
#         X = dx[i] + x
#         Y = dy[i] + y
#         if X >= M or X < 0 or Y >= N or Y < 0:
#             if graph[X][Y] == '.':
#                 return True
#             elif graph[X][Y] == 'O':
#                 return True
#         else:
#             return False
#         ## 사`방에 .가 아예 ㅇ벗는 경우엔 False
#     return False
# # def DFS(x, y):
# #     ## 1은 방문
# #
# #     global answer
# #     if graph[x][y] == 'O':
# #         return answer
# #     # if graph[x][y] == 'O' or '1' or '#':
# #     #     return
# #     else:
# #         for i in range(4):
# #             X = dx[i] + x
# #             Y = dy[i] + y
# #             ## 확인하는 함수
# #             if X >= M or X < 0 or Y >= N or Y < 0:
# #                 continue
# #             ## 탐색 방향이 바뀔때만 answer에 1씩 더해야
# #             if graph[X][Y] == '.' and check(X,Y):
# #                 graph[X][Y] = 1
# #                 DFS(X,Y)
# #             elif graph[X][Y] == '#' or 1:
# #                 if check(X,Y):
# #                     answer +=1
# #                 continue
# #             elif graph[X][Y] == 'O':
# #                 return answer
# #         ## 여기까지 내려왔다는건 움직일 수 없는 상태라는거니깐
# #         return
#
# def DFS(x,y):
#     ## 각 방향 끝까지 이동하는 함수를 다 쓰자
#     Right(x,y)
#     Left(x,y)
#     Up(x,y)
#     Down(x,y)
#     return
# for i in range(M):
#     for j in range(N):
#         if graph[i][j] == 'R':
#             DFS(i, j)
#
# for i in range(N):
#     for j in range(N):
#         print(graph[i][j], end='')
#     print('\n')
# print(answer)
# ## 리턴을 넣으니깐 그냥 DFS 자체를 탈출하네
from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()


def init():
    rx, ry, bx, by = [0] * 4  # 초기화 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':  # board에 빨간 구슬이라면 좌표 값 저장
                rx, ry = i, j
            elif board[i][j] == 'B':  # board에 파란 구슬이라면 좌표 값 저장
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))  # 위치 정보와 depth
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    init()
    while q:  # BFS -> queue, while
        rx, ry, bx, by, depth = q.popleft()  # FIFO
        if depth > 10:  # 10 이하여야 한다.
            break
        for i in range(len(dx)):  # 4방향으로 시도한다.
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])  # RED
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])  # BLUE

            if board[next_bx][next_by] == 'O':  # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if board[next_rx][next_ry] == 'O':  # 빨간 구슬이 구멍에 떨어진다면(성공)
                print(depth)
                return
            if next_rx == next_bx and next_ry == next_by:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth + 1))
    print(-1)  # 실패


bfs()


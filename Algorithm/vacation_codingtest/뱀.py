from collections import deque
N = int(input())
K  = int(input())
g = [[0] * N for _ in range(N)]
## 게임판에 사과표시
for _ in range(K):
    a,b = map(int,input().split())
    g[a-1][b-1] = 9
T = 0
key = 0
snake = deque()
snake.append((0,0))
## key값으로 몇번 명령을 돌렸는지를 파악하고 이에 해당하는 값을 DirectionKey에 저장한다.
DirectionKey = 3
## 이동경로 리스트
m = int(input())
action = ['0'] * 10001
for _ in range(m):
    c,d = input().split()
    action[int(c)] = d
## 뱀그리기

## 위, 왼쪽, 아래, 오른쪽
dx = [-1,0,1,0]
dy = [0,-1,0, 1]
## 초기값을 오른쪽으로 둘것인가
## D명령이 들어오면
D = [3,2,1,0]
## C명령이 드렁오면
C = [3,0,1,2]
while True:
    ## 이동방향으로 1을 먼저 칠하고 만약에 사과를 먹지 못하면
    ## 가장 끝점을 지우면 된다
    if action[T] != '0':

        if action[T] == 'D':
            key = D.index(DirectionKey)
            key += 1
            if key >3:
                key %= 4
                DirectionKey = D[key]
            else:
                DirectionKey = D[key]
        if action[T] == 'L':
            key = C.index(DirectionKey)
            key += 1
            if key > 3:
                key %= 4
                DirectionKey = C[key]
            else:
                DirectionKey = C[key]
    T += 1
    ## 대가리
    x,y = snake.pop()
    ## 오른쪼긍면 0, 1이 되겠지
    nx, ny  = x+ dx[DirectionKey] , y + dy[DirectionKey]
    ## 벽에 부딫히는지 아닌지 체크
    if N > nx >=0 and N > ny >= 0 and (nx,ny) not in snake:
        snake.append((x,y))
        snake.append((nx,ny))
        if g[nx][ny] != 9:
            snake.popleft()
        elif g[nx][ny] == 9:
            g[nx][ny] = 0
    else:
        break

print(T)
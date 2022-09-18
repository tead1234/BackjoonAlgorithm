## 이문제의 가장 큰 핵심은 파란구슬과 빨간구슬의 움직임을 동시에 구현해야한다는 점
## 한방향으로 계속 움직여야하니깐 dfs가 맞음
## 몇번 기울였는지를 파악하는 depth와 구슬의 이동거리를 이용해서 재조정하는 과정이 필요함
## 각 공을 따로 움직이지말고 같이 움직여야함
## 0쪽으로 가야하는데 bfs나 dfs 어떤걸써야
## 일단 이동할수 있는 모든 방향을 찾고 그중에서 0가 있다면 그쪽으로 이동하도록 짜야하나나
from collections import deque
N,M = map(int,input().split())
## 최단거리를 찾아야하니깐 한칸씩이동시키지말고 끝까지 이동시키는 bfs를 쓰면될듯
G = [list(input()) for _ in range(N)]
depth  = 0
loc_R = (0,0)
loc_B = (0,0)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def keepgoing(x,y,nx,ny):
    next_x = x
    next_y = y
    cnt = 0
    ## 범위 제한 넣어야됨
    while G[x+nx][y+ny] != 'O' or G[x+nx][y+ny] != '#':
        next_x += nx
        next_y += ny
        cnt += 1
    return (next_x,next_y,cnt)


def move(loc_R, loc_B, depth):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((loc_R, loc_B, depth))
    x, y = loc_R
    z, w = loc_B
    ## 방문처리
    visited[x][y] = 1
    visited[z][w] = 1

    while q:
        if depth > 10:
            return False
        depth += 1
        RED,BLUE, depth = q.popleft()
        rx, ry = RED
        bx, by = BLUE
        for k in range(4):
            ## 현재 방향이랑 다음 방향을 던져주면
            nx = dx[k]
            ny = dy[k]
            ## 범위 안에서 놀아야되는데 그걸 캐치 안했구나
            if N>rx + nx>=0 and M>ry + ny>=0 and G[rx + nx][ry + ny] != '#':
                ## 방향하나를 정하고 가능하면 그방향으로 쭉 이동시키고 q에 추가 시키기
                next_rx, next_ry, R_cnt = keepgoing(rx, ry, nx, ny)
            if N>rx + nx>=0 and M>ry + ny>=0 and G[bx + nx][by + ny] != '#':
                next_bx, next_by, B_cnt = keepgoing(bx, by, nx, ny)
            ## 함수로 나온 값이 visited로 체크된 곳이면 그냥 원상복귀를 시키는게 맞겠지???
            ## 만약에 레드가 이동하다가 0을 만나서 나온거면 거기서 종료
            ## 블루가 이동하다가 o을 만난거라면 마찬가지로 종료
            ## R_cnt > Bcnt> next에서 nxny만큼 뺴고 방문으로 마킹
            if G[next_rx][next_ry] == 'O':
                if G[next_bx][next_by] != 'O':
                    return True
            else:
                ## 위치가 겹칠경구
                if next_rx == next_bx and next_ry == next_by:
                    if R_cnt > B_cnt:
                        visited[next_rx - nx][next_ry - ny] = 1
                        visited[next_bx][next_by] = 1
                        q.append((next_rx - nx, next_ry - ny, next_bx, next_by, depth))
                    else:
                        visited[next_bx - nx][next_by - ny] = 1
                        visited[next_rx][next_ry] = 1
                        q.append((next_rx, next_ry, next_bx - nx, next_by - ny, depth))
                # 안겹치면 그냥 큐에 때려박기
                else:
                    visited[next_bx][next_by] = 1
                    visited[next_rx][next_ry] = 1
                    q.append((next_rx, next_ry, next_bx, next_by, depth))
    return False
for i in range(N):
    for j in range(M):
        if G[i][j] == 'R':
            loc_R = (i,j)
        if G[i][j] == 'B':
            loc_B =  (i,j)
if move(loc_R,loc_B,depth):
    print(1)
else:
    print(0)





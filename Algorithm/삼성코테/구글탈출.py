from collections import deque
N,M = map(int,input().split())
G = [list(input()) for _ in range(N)]
depth  = 0
## visited 배열이 없어서 그런거 같은데
## 각 경우마다 빨간공과 파란공의 위치를 저장하는 visited 배열이 필요함
## visited[1][1]이면 1회 움직였을떄 0,1,2,3 상 왼 아 오 방향으로 움직였을떄 위치를 저장하는 배열
## 결국 2차원 배열속에 2차월 배열이 들어가야 되네
## 4차우너 배열이 필요한 이유
visited_R = [[0] * M for _ in range(N)]
visited_B = [[0] * M for _ in range(N)]


dx = [-1,0,1,0]
dy = [0,-1,0,1]

def keepgoing(x,y,nx,ny):
    cnt = 0
    ## 범위 제한 넣어야됨
    while (N-1>x+nx>0 and M-1>y+ny>0) and G[x][y] != 'O' and G[x][y] != '#':
        x += nx
        y += ny
        cnt += 1
    return (x,y,cnt)
def move(x,y, z,w, depth):
    q = deque()
    q.append((x,y, z,w, depth))
    visited_R[x][y] = 1
    visited_B[z][w] = 1
    while q:
        rx, ry,bx, by, depth = q.popleft()
        if depth > 10:
            return False

        for k in range(4):
            nx = dx[k]
            ny = dy[k]
            next_bx = bx
            next_by = by
            next_rx = rx
            next_ry = ry
            R_cnt = 0
            B_cnt = 0
            if N>rx + nx>=0 and M>ry + ny>=0 and G[rx + nx][ry + ny] != '#':
                next_rx, next_ry, R_cnt = keepgoing(rx, ry, nx, ny)
            if N>bx + nx>=0 and M>by + ny>=0:
                if G[bx + nx][by + ny] != '#':
                    next_bx, next_by, B_cnt = keepgoing(bx, by, nx, ny)
            if visited_R[next_rx][next_ry] == 1:
                next_rx = rx
                next_ry = ry
            if visited_B[next_bx][next_by] == 1:
                next_by =by
                next_bx =bx
            if G[next_rx][next_ry] == 'O':
                if G[next_bx][next_by] != 'O':
                    return True
            else:

                if next_rx == next_bx and next_ry == next_by:
                    if R_cnt > B_cnt:
                        q.append((next_rx - nx, next_ry - ny, next_bx, next_by, depth+1))
                        visited_R[next_rx - nx][next_ry - ny] = 1
                        visited_B[next_bx][next_by] = 1
                    else:
                        visited_B[next_bx - nx][next_by - ny] = 1
                        visited_R[next_rx][next_ry] =1
                        q.append((next_rx, next_ry, next_bx - nx, next_by - ny, depth+1))
                else:

                    q.append((next_rx, next_ry, next_bx, next_by, depth+1))
                    visited_R[next_rx][next_ry] = 1
                    visited_B[next_bx][next_by] = 1
    return False
for i in range(N):
    for j in range(M):
        if G[i][j] == 'R':
            x,y = i,j
        if G[i][j] == 'B':
            z,w = i,j
if move(x,y,z,w,depth):
    print(1)
else:
    print(0)





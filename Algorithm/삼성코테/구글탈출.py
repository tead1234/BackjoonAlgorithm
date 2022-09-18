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

for i in range(N):
    for j in range(M):
        if G[i][j] == 'R':
            loc_R = (i,j)
        if G[i][j] == 'B':
            loc_B =  (i,j)

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def move(loc_R,loc_B,depth):
    q = deque()
    q.append((loc_R,loc_B,depth))
    r_cnt = 0
    b_cnt = 0
    while q:
        rx,ry,bx,by,depth = q.popleft()
        for k in range(4):
            next_rx =


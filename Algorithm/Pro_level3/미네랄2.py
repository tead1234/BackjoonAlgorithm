from collections import deque
import heapq
N, M = map(int, input().split())
G = [list(input()) for _ in range(N)]
k = int(input())
destroy = list(map(int, input().split()))
left = True
right = False


def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    vis = [(i, j)]
    visited[i][j] = 1
    while q:
        a, b = q.popleft()
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for k in range(4):
            c = a + dir[k][0]
            d = b + dir[k][1]
            if N > c >= 0 and M > d >= 0:
                if visited[c][d] != 1 and G[c][d] == 'x':
                    visited[c][d] = 1
                    q.append((c, d))
                    # vis.append((c,d))
                    heapq.heappush(vis, (-c,d))

    flg = False
    while flg == False:
        vis_2 = []

        flg2 = False
        if vis[0][0]  == -(N-1):
            break
        for vi in vis:
            v_x, v_y = vi
            v_x = v_x * -1
            if G[v_x+1][v_y] == 'x':
                flg = True
                break
            G[v_x][v_y] = '.'
            G[v_x+1][v_y] = 'x'
            vis_2.append((v_x + 1, v_y))
        vis = vis_2



    # 중력으로 떨구기


for i in range(k):
    destroy_row = destroy[i]

    if left:
        for a in G[N - destroy_row]:
            if a == 'x':
                G[N - destroy_row][G[N - destroy_row].index(a)] = '.'
                break
        left = False
        right = True
    elif right:
        for a in range(len(G[N - destroy_row]) - 1, -1, -1):
            if G[N - destroy_row][a] == 'x':
                G[N - destroy_row][a] = '.'
                break
        left = True
        right = False
    ## 클러스터 구하기
    ## g를 탐색해서 x면 bfs를 돌려서 구하고 아래로 떨구기
    vis = [[0] * M for _ in range(N)]
    for I in range(N):
        for J in range(M):
            if G[I][J] == 'x' and vis[I][J] != 1:
                bfs(I, J, vis)

for g in G:
    print("".join(g))

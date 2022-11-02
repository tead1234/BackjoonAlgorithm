from collections import deque

N, M = map(int, input().split())
G = [list(input()) for _ in range(N)]
k = int(input())
destroy = list(map(int, input().split()))
left = True
right = False


def bfs(i, j):
    q = deque()
    q.append((i, j))
    vis = [(i, j)]
    while q:
        a, b = q.popleft()
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for k in range(4):
            c = a + dir[k][0]
            d = b + dir[k][1]
            if N > c >= 0 and M > d >= 0:
                if (c, d) not in vis and G[c][d] == 'x':
                    q.append((c, d))
                    vis.append((c,d))
    ## 땅바닥에 닿은게 있는지 없는지 조사하고
    # 닿았다면 pass 아니면 떨구기
    flg = False
    while flg == False:
        for vi in vis:
            v_x, v_y = vi
            if v_x == N - 1:
                flg = True
                break
        if flg:
            break
        vis_2 = []
        flg2 = False
        for vi in vis:
            v_x, v_y = vi

            G[v_x][v_y] = '.'
            G[v_x+1][v_y] = 'x'
            vis_2.append((v_x + 1, v_y))
        vis = vis_2
    return vis


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
    vis = []
    for I in range(N):
        for J in range(M):
            if G[I][J] == 'x' and (I,J) not in vis:
                vis +=bfs(I, J)
                print(vis)

for g in G:
    print(g)

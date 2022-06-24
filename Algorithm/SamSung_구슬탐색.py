ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(i, j, di, dj):
    cnt = 0
    while g[i+di][j+dj] != '#' and g[i][j] != 'O':
        i, j = i+di, j+dj
        cnt += 1 # 중력에 따라 움직인 거리
    return i, j, cnt
## 기울였을때 도착하는 곳을 리턴하도록 아예 만들면 되네 각 방향마다 따질게 아니라
## 쭉 이동하도록 만드는 bfs도 알아놔야 겠음
def play(ri, rj, bi, bj, d):
    queue = [(ri, rj, bi, bj, d)]
    visited.append((ri, rj, bi, bj))

    while queue:
        sri, srj, sbi, sbj, sd = queue.pop(0)
        if sd > 10: # 10번 이내에 성공하지 못한 경우
            return -1
        for di, dj in ds:
            nri, nrj, rcnt = move(sri, srj, di, dj) # 빨간 구슬이 벽에 부딪히거나 구멍에 도달 했을 때
            nbi, nbj, bcnt = move(sbi, sbj, di, dj) # 파란 구슬이 벽에 부딪히거나 구멍에 도달 했을 때
            if g[nbi][nbj] != 'O':
                if g[nri][nrj] == 'O':
                    return sd
                if nri == nbi and nrj == nbj: # 같은 위치에 있으면 안 되기 때문에
                    if rcnt > bcnt: # 빨간 구슬이 더 많이 움직였을 때 빨간 구슬을 한 칸 뒤로
                        nri, nrj = nri-di, nrj-dj
                    else: # 파란 구슬이 더 많이 움직였을 때 파란 구슬을 한 칸 뒤로
                        nbi, nbj = nbi-di, nbj-dj
                if (nri, nrj, nbi, nbj) not in visited:
                    visited.append((nri, nrj, nbi, nbj))
                    queue.append((nri, nrj, nbi, nbj, sd+1))
    return -1 # 빨간 구슬이 구멍에 도달하지 못했을 때

N, M = map(int, input().split())
g = [list(input()) for _ in range(N)]
visited = []

for i in range(N):
    for j in range(M):
        if g[i][j] == 'R':
            ri, rj = i, j
        if g[i][j] == 'B':
            bi, bj = i, j

res = play(ri, rj, bi, bj, 1)

print(res)
from collections import deque

N = int(input())
g = [list(input()) for _ in range(N)]
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = []
queue = deque()
answer = 0


## 적록색약이면 R하고 G를 같은 구역으로 탐색하고
## 아니면 각각분류

def bfsForNormal(x, y):
    global answer
    queue.append((x,y))
    visited.append((x, y))
    while queue:
        탐색위치x, 탐색위치y = queue.popleft()
        for dx, dy in ds:
            if g[탐색위치x + dx][탐색위치y + dy] == g[탐색위치x][탐색위치y] and 0<=(탐색위치x + dx) < N and 0<=(탐색위치y + dy)< N:
                if (탐색위치x + dx, 탐색위치y + dy) not in visited :
                    visited.append((탐색위치x + dx, 탐색위치y + dy))
                    queue.append((탐색위치x + dx, 탐색위치y + dy))
            else:
                continue
    answer += 1
    return answer

for i in range(N):
    for j in range(N):
        if g[i][j] == "R":
            bfsForNormal(i,j)

print(answer)
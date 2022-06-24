from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
queue = deque()
visited = []
visited2 = []
answer = 0
answer2 = 0
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
ds = [(-1,0),(0,1),(1,0),(0,-1)]
def dfsForNormal(x,y):
    global answer
    if graph[x][y] not in visited:
        visited.append((x,y))
        queue.append((x,y))
        while queue:
            x ,y = queue.popleft()
            for dx, dy in ds:
                if  N> (x+dx) >= 0:
                    if N> (y+dy) >= 0:
                        if graph[(x+dx)][(y+dy)] == graph[x][y]:
                            if ((x+dx),(y+dy)) not in visited:
                                visited.append(((x+dx),(y+dy)))
                                queue.append(((x+dx),(y+dy)))
        answer += 1

    else:
        return
def dfsForUnNormalInBlue(x,y):
    global answer2
    if graph[x][y] not in visited2:
        visited.append((x,y))
        queue.append((x,y))
        while queue:
            x ,y = queue.popleft()
            for dx, dy in ds:
                if  N> (x+dx) >= 0:
                    if N> (y+dy) >= 0:
                        if graph[x][y] == 'B':
                            if graph[(x+dx)][(y+dy)] == graph[x][y]:
                                if ((x+dx),(y+dy)) not in visited2:
                                    visited2.append(((x+dx),(y+dy)))
                                    queue.append(((x+dx),(y+dy)))
                        else:
                            if graph[(x + dx)][(y + dy)] != 'B':
                                if ((x + dx), (y + dy)) not in visited2:
                                    visited2.append(((x + dx), (y + dy)))
                                    queue.append(((x + dx), (y + dy)))

        answer2 += 1

    else:
        return

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            if (i,j) not in visited:
                dfsForNormal(i,j)
            elif (i,j) not in visited2:
                dfsForUnNormalInBlue(i,j)
        if graph[i][j] == 'B':
            if (i,j) not in visited:
                dfsForNormal(i,j)
            elif (i, j) not in visited2:
                dfsForUnNormalInBlue(i, j)
        if graph[i][j] == 'G':
            if (i,j) not in visited:
                dfsForNormal(i,j)
            elif (i, j) not in visited2:
                dfsForUnNormalInBlue(i, j)

print(answer, answer2)
## 그래프 탐색후 해당 그래프 위치와 같은 글자를 가진 곳을 하나씩 묶은다음 answer에 탐색이 끝나면 1씩 더해주면되네
from collections import deque

n, m = map(int, input().split())

graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= m or y >= n:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer +=1

print(answer)
graph = [[0, 0, 0],
         [1, 0, 1],
         [0, 0, 2]]
## 좌 위 우 아래
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

answer = 0
def DFS(x, y, graph, answer):
    graph[x][y] = 1
    for i in range(4):

        X = dx[i] + x
        Y = dy[i] + y

        if 3 > X >= 0 and 3 > Y >= 0:
            if graph[X][Y] == 2:
                return answer
            if graph[X][Y] == 0:
                DFS(X, Y)
                answer += 1
                return
        ## 1이거나 범위를 벗어나는경우
        else:
            continue

print(DFS(0,0,graph,0))

from collections import deque

n,m = map(int,input().split())
graph =[]
queue = deque()
answer = 0
dx = [0,1]
dy=  [1,0]
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    global answer
    graph.append((x,y))
    while queue:
        v = queue.popleft()
        if graph[v[0]][v[1]] == 0:
            return
        if graph[v[0]][v[1]] == 1:
            answer += 1
        for i in range(2):
            X = dx[i] + v[0]
            Y = dy[i] + v[1]
            queue.append((X,Y))
    return answer

print(bfs(0,0))

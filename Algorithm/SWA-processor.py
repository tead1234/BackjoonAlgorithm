from collections import deque
K = int(input())
graph = [list(map(int,input().split())) for _ in range(K)]
## 1이 있으면 queue에 넣기
process = 0
link = 0
queue = deque()
for i in range(K):
    for j in range(K):
        if graph[i][j] == 1:
            queue.append((i,j))


## dfs요구조건
## queue에 나온 애를 시작점으로 탐색, 리턴되는 값은 link의 숫자와 process갯수

def dfs(x,y):
    global link
    global process
    ## y = 2인데 x가 -2여도 걸리네 시벌
    # 아래 조건에 걸리면 다음 큐에 있는 놈으로 넘어가야하는데
    if (x == 0 and K>y>=0) or (y ==0 and K>x>=0) or (x == K-1 and K>y>=0)  or (y == K-1 and K>x>=0):
        if graph[x][y] == 1:
            graph[x][y] = 2
            process += 1
            return
        if graph[x][y] == 0:
            graph[x][y] = 2
            link += 1
            process += 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

    if x>= K or y>= K or x < 0 or y< 0 or graph[x][y] == 2:
        return
    if graph[x][y] == 1 or 0:
        graph[x][y] = 2
        link +=1
        process += 1
        dfs(x-1,y)
        dfs(x , y -1)
        dfs(x+1, y)
        dfs(x, y + 1)

## 문제 queue에서 팝을 하니깐 하나씩
while queue:
    x,y = queue.popleft()
    dfs(x,y)

    print(process, link)
    process = 0
    link = 0

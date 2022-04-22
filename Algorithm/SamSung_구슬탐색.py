from collections import deque

M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input()))
queue = deque()
## 오른쪽, 위쪽, 왼쪽, 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
answer = 0
## 백트래킹을 할때마다 +1 을 해주면 해결될거같은데
## dfs는 일단 이동하고 판단하는건데
## check는 이동할 곳의 미래를 한번더 파악함 즉 dfs를 두번 연속으로 하는 것과 같은효과
def check(x,y):
    for i in range(4):
        X = dx[i] + x
        Y = dy[i] + y
        if X >= M or X < 0 or Y >= N or Y < 0:
            if graph[X][Y] == '.':
                return True
            elif graph[X][Y] == 'O':
                return True
        else:
            return False
        ## 사`방에 .가 아예 ㅇ벗는 경우엔 False
    return False
def DFS(x, y):
    ## 1은 방문

    global answer
    if graph[x][y] == 'O':
        return answer
    # if graph[x][y] == 'O' or '1' or '#':
    #     return
    else:
        for i in range(4):
            X = dx[i] + x
            Y = dy[i] + y
            ## 확인하는 함수
            if X >= M or X < 0 or Y >= N or Y < 0:
                continue
            ## 탐색 방향이 바뀔때만 answer에 1씩 더해야
            if graph[X][Y] == '.' and check(X,Y):
                graph[X][Y] = 1
                DFS(X,Y)
            elif graph[X][Y] == '#' or 1:
                if check(X,Y):
                    answer +=1
                continue
            elif graph[X][Y] == 'O':
                return answer
        ## 여기까지 내려왔다는건 움직일 수 없는 상태라는거니깐
        return


for i in range(M):
    for j in range(N):
        if graph[i][j] == 'R':
            DFS(i, j)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end='')
    print('\n')
print(answer)
## 리턴을 넣으니깐 그냥 DFS 자체를 탈출하네
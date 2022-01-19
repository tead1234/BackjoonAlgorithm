from collections import deque
K = int(input())
graph = [list(map(int,input().split())) for _ in range(K)]
graph_v = [[0 for _ in range(K)] for _ in range(K)]
for i in range(K):
    for j in range(K):
        graph_v[i][j] = graph[i][j]
## 1이 있으면 queue에 넣기
process = False
link1 = 0
link2 = 0
link3 = 0
link4 = 0


queue = deque()
link_sum = 0
process_sum = 0
for i in range(K):
    for j in range(K):
        if graph[i][j] == 1:
            queue.append((i,j))

## dfs요구조건
## queue에 나온 애를 시작점으로 탐색, 리턴되는 값은 link의 숫자와 process갯수
def right(x,y):

    global process
    global link1
    if x >= K or y >= K or x < 0 or y < 0:
        if link1 != 0:
            process = True
            return True

    if graph[x][y] == 2 or graph[x][y] == 1:
        link1 = 0
        process = False
        return

    if graph[x][y] == 0:
        graph[x][y] = 2
        link1 +=1
        right(x, y + 1)
def left(x,y):

    global process
    global link2
    if x >= K or y >= K or x < 0 or y < 0:
        if link2 != 0:
            process = True
            return True



    if graph[x][y] == 2 or graph[x][y] == 1:
        link2 = 0
        return

    if graph[x][y] == 0 :
        graph[x][y] = 2
        link2 += 1
        print(link2)
        left(x, y - 1)
def up(x,y):

    global process
    global link3
    if x >= K or y >= K or x < 0 or y < 0:
        if link3 != 0:
            process = True
            return True


    if graph[x][y] == 2 or graph[x][y] == 1:
        link3 = 0
        return

    if graph[x][y] == 0:
        graph[x][y] = 2
        ## 여기서 무조건 +1이 되니깐 마지막에 -1 해줘야
        link3 += 1
        up(x -1, y)
def down(x,y):
    global link4
    global process

    if x >= K or y >= K or x < 0 or y < 0:
        if link4 != 0:
            process = True
            return True
    if graph[x][y] == 2 or graph[x][y] == 1:
        link4 = 0
        return

    if graph[x][y] == 0:
        graph[x][y] = 2
        link4 += 1
        down(x + 1, y)
def dfs(x,y):
    global link
    global process
    global link1
    global link2
    global link3
    global link4
    global link_sum
    global process_sum

    ## y = 2인데 x가 -2여도 걸리네 시벌
    # 아래 조건에 걸리면 다음 큐에 있는 놈으로 넘어가야하는데
    if graph[x][y] == 1:
        if (x == 0 and K > y >= 0) or (y == 0 and K > x >= 0) or (x == K - 1 and K > y >= 0) or (
                y == K - 1 and K > x >= 0):
            graph[x][y] = 2
            process_sum += 1
            return
        graph[x][y] = 2
        if left(x,y-1) == True:

            process = False


        if up(x -1 , y ) == True:

            process = False
        if right(x , y + 1) == True:

            process = False

        if down(x + 1, y) == True:

            process = False
        if left(x,y) == True or up(x , y ) == True or right(x, y) == True or down(x, y ) == True:
            ## 여기중에서  0값을 제외해야됨
            # m
            sorlist = [link1,link3,link2,link4]
            for c in range(4):
                if sorlist[c] == 0:
                    sorlist.remove(sorlist[c])
            link = min(sorlist)
            link_sum += link
            process_sum += 1
            link = 0
            link1 = 0
            link2 = 0
            link3 = 0
            link4 = 0
## 문제 queue에서 팝을 하니깐 하나씩
# 그럼 여기서
for _ in range(len(queue)):
    a,b = queue.popleft()
    queue.append((a,b))
    for i in range(K):
        for j in range(K):
            graph[i][j] = graph_v[i][j]
    ## 아래가 큐안에 들어있는 상태로 한번 루프 돌리는거
    for i in range(len(queue)):
        x,y = queue[i]
        dfs(x,y)
    print(link_sum, process_sum)
    link_sum = 0
    process_sum = 0





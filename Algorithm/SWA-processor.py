from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    graph = [list(map(int, input().split())) for _ in range(K)]
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
    addProcess = 0
    min_link_sun =100000
    max_process = 0
    for i in range(K):
        for j in range(K):
            if graph[i][j] == 1:
                queue.append((i, j))


    ## dfs요구조건
    ## queue에 나온 애를 시작점으로 탐색, 리턴되는 값은 link의 숫자와 process갯수
    def right(x, y):
        global process
        global link1
        if x >= K or y >= K or x < 0 or y < 0:
            if link1 != 0:
                process = True
                return True

        if graph[x][y] == 2 or graph[x][y] == 1:
            link1 = 0
            process = False
            return False

        if graph[x][y] == 0:
            link1 += 1
            right(x, y + 1)
        return True


    def left(x, y):
        global process
        global link2
        if x >= K or y >= K or x < 0 or y < 0:
            if link2 != 0:
                process = True
                return True

        if graph[x][y] == 2 or graph[x][y] == 1:
            link2 = 0
            return False

        if graph[x][y] == 0:
            link2 += 1
            left(x, y - 1)
        return True


    def up(x, y):
        global process
        global link3
        if x >= K or y >= K or x < 0 or y < 0:
            if link3 != 0:
                process = True
                return True

        if graph[x][y] == 2 or graph[x][y] == 1:
            link3 = 0
            return False

        if graph[x][y] == 0:
            ## 여기서 무조건 +1이 되니깐 마지막에 -1 해줘야
            link3 += 1
            up(x - 1, y)
        return True


    def down(x, y):
        global link4
        global process

        if x >= K or y >= K or x < 0 or y < 0:
            if link4 != 0:
                process = True
                return True
        if graph[x][y] == 2 or graph[x][y] == 1:
            link4 = 0
            return False

        if graph[x][y] == 0:
            link4 += 1
            down(x + 1, y)
        return True


    def draw_right(x, y):
        if x >= K or y >= K or x < 0 or y < 0:
            return

        if graph[x][y] == 2 or graph[x][y] == 1:
            return

        if graph[x][y] == 0:
            graph[x][y] = 2
            draw_right(x, y + 1)
        return
    def draw_left(x, y):
        if x >= K or y >= K or x < 0 or y < 0:
            return

        if graph[x][y] == 2 or graph[x][y] == 1:
            return

        if graph[x][y] == 0:
            graph[x][y] = 2
            draw_left(x, y - 1)
        return
    def draw_up(x, y):
        if x >= K or y >= K or x < 0 or y < 0:
            return

        if graph[x][y] == 2 or graph[x][y] == 1:
            return

        if graph[x][y] == 0:
            graph[x][y] = 2
            draw_up(x - 1, y)
        return
    def draw_down(x, y):
        if x >= K or y >= K or x < 0 or y < 0:
            return

        if graph[x][y] == 2 or graph[x][y] == 1:
            return

        if graph[x][y] == 0:
            graph[x][y] = 2
            draw_down(x + 1, y)
        return

    def dfs(x, y):
        global link
        global process
        global link1
        global link2
        global link3
        global link4
        global link_sum
        global process_sum
        global addProcess
        ## y = 2인데 x가 -2여도 걸리네 시벌
        # 아래 조건에 걸리면 다음 큐에 있는 놈으로 넘어가야하는데
        if graph[x][y] == 1:
            if (x == 0 and K > y >= 0) or (y == 0 and K > x >= 0) or (x == K - 1 and K > y >= 0) or (
                    y == K - 1 and K > x >= 0):
                graph[x][y] = 2
                process_sum += 1
                return
            graph[x][y] = 2

            if left(x, y - 1) == True and process ==True:
                addProcess += 1
                process = False

            if up(x - 1, y) == True and process ==True:
                addProcess += 1
                process = False
            if right(x, y + 1) == True and process ==True:
                addProcess += 1
                process = False

            if down(x + 1, y) == True and process ==True:
                addProcess += 1
                process = False
            ### 프로세스가 어디서든 트루값이 하나라도 있으면

            if addProcess > 0 and addProcess <= 4:
                process_sum += 1
                addProcess = 0
            else:
                addProcess = 0
            linkList = [link1, link2, link3, link4]
            linkList2 = [i for i in linkList if i != 0]
            try:
                link = min(linkList2)
                link_sum += link
                if link == link1:
                    draw_right(x, y + 1)
                elif link == link2:
                    draw_left(x,y-1)
                elif link == link3:
                    draw_up(x-1,y)
                elif link == link4:
                    draw_down(x+1,y)
                link = 0
                link1 = 0
                link2 = 0
                link3 = 0
                link4 = 0
            except:
                link = 0
                link_sum += link


    ## 문제 queue에서 팝을 하니깐 하나씩
    # 그럼 여기서
    for _ in range(len(queue)):
        a, b = queue.popleft()
        queue.append((a, b))
        for i in range(K):
            for j in range(K):
                graph[i][j] = graph_v[i][j]
        ## 아래가 큐안에 들어있는 상태로 한번 루프 돌리는거
        for i in range(len(queue)):
            x, y = queue[i]
            dfs(x, y)
        ### 맥스는 바뀌는데 min이 안바뀌네
        if process_sum > max_process:
            max_process = process_sum
            min_link_sun = link_sum
        if process_sum == max_process:
            if min_link_sun >= link_sum:
                min_link_sun = link_sum
        link_sum = 0
        process_sum = 0
    print("#{}".format(test_case),min_link_sun)
    max_process = 0
    min_link_sun = 100000

## 문제 발견 .... 지금 탐색한 부분 전부를 2로 칠해놓으니 다음 점에서 탐색할때 걸림 시발...
# 왠지는 모르겠는데 process수가 늘어남 왲::::/?

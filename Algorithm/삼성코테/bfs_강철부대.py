from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    q = deque()
    roadList = [[] for _ in range(n+1)]
    flag = False
    for ro in roads:
        a, b = ro
        roadList[a].append(b)
        roadList[b].append(a)
    def bfs(start,desti, answer):
        global flag
        dist= [0] * (n+1)
        vis = [False] * (n+1)
        q.append(start)
        vis[start] = True
        while q:
            x= q.popleft()
            if x == desti:
                flag = True
                answer.append(dist[x])
            ## x는 시작점
            for next in roadList[x]:
                if vis[next] == False:
                    dist[next] = dist[x] + 1
                    q.append(next)
                    vis[next] = True
        if flag == False:
            answer.append(-1)
        if flag:
            flag = False
    for sour in sources:
        bfs(sour, destination,answer)

    return answer


solution(5,[[1,2],[1,4],[2,4],[2,5],[4,5]], [1,3,5], 5)
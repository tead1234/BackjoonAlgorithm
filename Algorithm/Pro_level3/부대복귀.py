import sys
from collections import deque


## 그냥 bfs 로 해결 될거같은데
def bfs(start, end, n, Map):
    q = deque()
    dist = [False] * n
    ans = 951584184
    # 초기화
    q.append([start - 1, 0])
    dist[start - 1] = True
    ## 비용이 다르다면 dist배열을 이차원으로 하는게 맞음 >> 방문했던곳이라도 더 적은 비용으로 방문이 가능할 수 있기때문
    while q:
        pre, pre_dist = q.popleft()
        if pre == end - 1 and ans > pre_dist:
            ans = pre_dist
        for i in Map[pre]:
            if dist[i] == False:
                dist[i] = True
                q.append([i, pre_dist + 1])
    if ans != 951584184:
        return ans
    else:
        return -1


def solution(n, roads, sources, destination):
    answer = []
    Map = [[] for _ in range(n)]
    for road in roads:
        a, b = road
        Map[a - 1].append(b - 1)
        Map[b - 1].append(a - 1)
    # print(Map)
    for s in sources:
        # print(s)
        answer.append(bfs(s, destination, n, Map))

    return answer
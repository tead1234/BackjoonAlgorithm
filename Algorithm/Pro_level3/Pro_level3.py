import heapq


## bfs를 돌리면 모든 꼭지점에서 한번씩 다 돌려야 됨
## 완전탐색같은데
ans = 0
def bfs(start, G, visited):

    q = []
    heapq.heappush(q, start)
    global ans
    while q:
        # 길이랑 인덱스
        L, I = heapq.heappop(q)
        visited[I] = True
        ans += L
        if not False in visited:
            return True
        else:
            for next in G[I]:
                nL, nI = next
                if visited[nI]:
                    continue
                else:
                    heapq.heappush(q, next)
    return False


def solution(n, costs):
    global ans
    answer = []

    G = [[] for _ in range(n)]
    ## dic으로 풀어볼까?
    # dic은 키값으로 a, b를 가지게 담들면
    dic = {}
    visited = [False] * n
    for cost in costs:
        a, b, c = cost
        if a not in dic.keys():
            dic[a] = []
            dic[a].append((c,b))
        if b not in dic.keys():
            dic[b] = []
            dic[b].append((c, a))
        elif a in dic.keys():
            dic[a].append((c,b))
        elif b in dic.keys():
            dic[b].append((c, a))

        # G[a].append((c, b))
        # G[b].append((c, a))

    for i, g in enumerate(G):
        ans = 0
        visited[i] = True
        if bfs(sorted(g)[0], , visited):
            answer.append(ans)
        visited = [False] * n


    return min(answer)

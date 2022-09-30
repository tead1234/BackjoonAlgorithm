import heapq
import copy

## 다익스트라인데
## 각 노드에서 가장 시간이 짧게 걸리는 애들만 우선순위로 가면 되징낳나?
## 정상에서 최소값을 가진애들만 가면되겠네
## 각 정상마다 한번씩 다돌려야됨
## 걍 dfs인듯
def solution(n, paths, gates, summits):
    answer = []
    gates = set(gates)

    least = []
    summits = set(summits)
    ## 연결 그래프
    # G[0] = 1번 봉우리
    G = [[] for _ in range(n)]
    for p in paths:
        a, b, l = p
        heapq.heappush(G[a - 1], (l, b - 1))
        heapq.heappush(G[b - 1], (l, a - 1))
    Summits = [0] * (n + 1)

    for Su in summits:
        Summits[Su] += 1

    def dfs(n, L, GC):
        # 방문처리

        visited[n] = 1
        if n + 1 in gates:
            answer.append(L)
            return

        # 해당ㅇ노드에 연결된 모든 점여기서 he
        while GC[n]:
            a, b = heapq.heappop(GC[n])

            if visited[b] == 1:
                continue
            if Summits[b + 1] == 1:
                continue
            else:
                if L < a:

                    dfs(b, a,GC)
                else:
                    dfs(b, L, GC)
                visited[b] = 0

    for S in summits:
        GC = copy.deepcopy(G)
        visited = [0] * n
        ans = []
        ans.append(S)
        dfs(S - 1, 0, GC)
        ans.append(min(answer))
        least.append(ans)
        least = sorted(least, key=lambda x: (x[1], x[0]))

    return least[0]

#
# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
#                , [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1,5]))

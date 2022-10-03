from collections import deque

m = 0
def solution(n, edge):
    answer = [0] * (n + 1)

    G = [[] for _ in range(n)]
    for ED in edge:

        a, b = ED
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    def bfs(end):
        global m
        q = deque()
        q.append((0, 0))
        visited = [0] * n
        visited[0] = 1
        while q:
            next, depth = q.popleft()

            if next + 1 == end:
                if m < depth:
                    m = depth
                answer[next] = depth
                break
            else:
                for g in G[next]:
                    if visited[g] == 0:
                        q.append((g, depth + 1))


    for i in range(2, n + 1):
        bfs(i)

    ans = 0
    for a in answer:
        if a == m:
           ans += 1
    return ans

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
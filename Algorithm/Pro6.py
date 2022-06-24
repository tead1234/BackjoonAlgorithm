from collections import deque


def bfs(x, y, n, computers):
    queue = deque()
    visited = []
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()
        visited.append((a, b))
        for i in range(n):
            if computers[b][i] == 1:
                if i not in visited:
                    queue.append((b, i))
                    computers[b][i] = 0



def solution(n, computers):
    answer = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                bfs(i, i, n, computers)
                answer += 1
    return answer


print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))

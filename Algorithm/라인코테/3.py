## 전형적인 bfs 문제네
from typing import List
from collections import deque


def Icebfs(x, y):
    pass


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[]]
    direct = []
    direct2 = []
    visited = [[0] * n for _ in range(n)]
    visited2 = [[0] * n for _ in range(n)]

    def Firebfs(x, y, m):
        q = deque()

        visited[x][y] = 0
        q.append((x, y))
        ## 불꽃 방향
        k = 0
        while q:
            if k == m:
                break
            k += 1
            a, b = q.popleft()
            ## 나올 방향을 전부 찾기
            for i in range(-k, k + 1):
                for j in range(-k, k + 1):
                    direct.append((i, j))
            for p in range(len(direct)):
                X = a + direct[p][0]
                Y = b + direct[p][1]
                if n > X >= 0 and n > Y >= 0:
                    q.append((X, Y))
                    visited[X][Y] = visited[X][Y] + 1

    for fire in fires:
        Firebfs(fire[0]-1, fire[1]-1, m)

    print(visited)
    return answer
print(solution(3, 2, [[1, 1]], [[3, 3]]))
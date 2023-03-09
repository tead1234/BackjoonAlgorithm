from collections import deque

n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
t = 0
destinations = [list(map(int, input().split())) for _ in range(m)]


def findNearest(x, y, Map):
    q = deque()
    Map[x][y] = 0
    q.append((x, y))
    desi = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = []
    while q:
        a, b = q.popleft()
        print(q)
        for i in range(4):
            A = a + desi[i][0]
            B = b + desi[i][1]
            if 0 <= A < n and 0 <= B < n:
                if Map[A][B] == 1:
                    ans.append((Map[a][b] + 1, A, B))
                elif Map[A][B] == 0:
                    q.append((A, B))
                    Map[A][B] = Map[a][b] + 1
    return ans


print(findNearest(1, 2, Map.copy()))

from collections import deque
def solution(m, n, puddles):
    answer = 0
    dist = [[0] * m for _ in range(n)]
    # 출발점
    dist[0][0] = 0
    q = deque()
    for pud in puddles:
        x,y = pud
        dist[x-1][y-1] = "E"
    q.append((0,0))
    while q:
        a,b = q.popleft()
        if a == n-1 and b == m-1:
            answer = dist[n - 1][m - 1] % 100000007
            return answer
        dx = [(1,0), (0,1)]
        for k in range(2):
            if n > dx[k][0] + a >=0 and m > dx[k][1] + b >= 0:
                if dist[dx[k][0] + a][dx[k][1] + b] == "E":
                    continue
                q.append((dx[k][0] + a,dx[k][1] + b))
                dist[dx[k][0] + a][dx[k][1] + b] += 1


print(solution(4,3,[[2,2]]))
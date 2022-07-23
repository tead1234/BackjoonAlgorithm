from collections import deque
def bfs(x,n):
    q = deque()
    q.append(x)
    ans = 0
    while q:
        x = q.popleft()
        if x + 1 < n:
            q.append(x+1)
        if x + 2 < n:
            q.append(x+2)
        elif x + 1 == n:
            ans += 1
        elif x + 2 == n:
            ans += 1
    return ans % 1000000007
def solution(n):
    answer = 0
    answer += bfs(1,n)
    answer += bfs(2,n)
    return answer


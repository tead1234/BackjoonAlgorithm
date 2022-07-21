from collections import deque
N = int(input())
app = deque(list(map(int,input().split())))
ans = []
def dfs(x, diff):

    if x == N:
        ans.append(diff)
        return
    elif x< N:
        dfs(x+1, diff + app[x])
        dfs(x+1, diff - app[x])

dfs(0,0)
g = list(map(abs,ans))
print(min(g))

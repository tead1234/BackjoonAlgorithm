N, M = map(int,input().split())
L = list(map(int,input().split()))
c = list(map(int,input().split()))
# 완탐이 맞는 듯 한데?
vis = [False] * (N)
test = []
ans = []
for x,y in zip(L,c):
    test.append([x,y])
for i in range(len(test)):
    test[i].append(i)
print(test)
def dfs(vis,cost,c_val,n):

    if cost >= M:
        ans.append(c_val)
        return
    else:
        # 처음 방문은 그냥 시작할떄 하는걸로
        for t in test:
            idx,a, b = t
            if vis[b] != True:
                vis[b] = True
                dfs(vis,cost+idx, c_val+ a, b)
                vis[b] = False
for i in range(N):
    vis[i] = True
    first,sen,third = test[i]
    dfs(vis,first,sen, third)
print(min(ans))
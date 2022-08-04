n,m = map(int,input().split())
List = [[] for _ in range (n+1)]
## n-1로 해야됨
color = [0] * n
for _ in range(m):
    a,b = map(int,input().split())
    List[a].append(b)
    List[b].append(a)

def dfs(x,C):
    ## 첫방문을 무조건 1로 칠함

    if color[x-1] != 0:
        if color[x-1] == C:
            return True
    else:
        color[x-1] = C
        for li in List[x]:
            if color[li-1] == 0:
                if C == 1:
                    D= 2
                else:
                    D = 1
                dfs(li, D)
    return False
# 안되면 true를 아무 이상없으면 false
a = False
for i in range(1,n+1):
    color = [0] * n
    if dfs(i,1):
        a = True

if a:
    print("NO")
else:
    print("YES")

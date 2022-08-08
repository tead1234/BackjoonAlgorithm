n = int(input())
List = [list(map(int,input().split())) for _ in range(n)]
ans = 0
ansList = []

def dfs(x,d):
    global ans
    if d == n:
        ansList.append(ans)
        return
    if d > n:
        return
    else:
        for next in List:
            time, wage,num = next
            if  d > num:
                continue
            else:
                ans += wage
                dfs(next,num+time)
                ans -= wage
            ansList.append(ans)
    return
for i,a in enumerate(List):
    a.append(i)
for a in List:
    t,w,m = a
    ans += w
    dfs(a,t+m)
    ans -= w
if len(ansList) ==0 :
    print(0)
else:
    print(max(ansList))

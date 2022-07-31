n,m = map(int,input().split())
## 이긴 배열
List = [[] for _ in range(n+1)]
vis = [False] * (n+1)
s= 0
sList= [0] * (n+1)
# 진배열
List2 = [[] for _ in range(n+1)]
s2 = 0
vis2 = [False] * (n+1)
sList2= []

for _ in range(m):
    a,b = map(int,input().split())
    List[a].append(b)
    List2[b].append(a)

def dfs(x, List, vis):
    global s
    ## dfs 구현 1. 종료 조건
## 2 아닐경우 돌아가는 반복문
## 3. 반복문에 재귀넣고 백트래킹은 어떻게 할것인지
    if vis[x]:
        return
    else:
        vis[x] = True
        ## x를 방문한 횟수가 아니라
        ## 나머지 후보들을 반복문
        for i in List[x]:
            if vis[i] == False:
                s+=1
                dfs(i,List, vis)

    return
def dfs2(x, List, vis):
    global s2
    ## dfs 구현 1. 종료 조건
## 2 아닐경우 돌아가는 반복문
## 3. 반복문에 재귀넣고 백트래킹은 어떻게 할것인지
    if vis[x]:
        return
    else:
        vis[x] = True
        ## x를 방문한 횟수가 아니라
        ## 나머지 후보들을 반복문
        for i in List[x]:
            if vis[i] == False:
                s2+=1
                dfs2(i,List, vis)
    return
for i in range (1,n+1):
    dfs(i,List, vis)
    sList[i] += s
    vis = [False] * (n + 1)
    s = 0

for i in range (1,n+1):
    dfs2(i,List2, vis2)
    sList[i] += s2
    vis2 = [False] * (n + 1)
    s2 = 0
ans = 0
for a in sList:
    if a ==n-1:
        ans += 1
print(ans)
# ans2 = [a+b for a,b in zip(sList,sList2)]
# print(ans2)

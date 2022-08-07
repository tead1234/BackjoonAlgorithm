n = int(input())
List = [list(map(int,input().split())) for _ in range(n)]
ans = 0
ansList = []
vis = [False] * n



def dfs(x,d):
    global ans
    if d > n:
        return
    else:
        ## 다음 탐색을 정할때 방문하지 않았던 애들만 탐색
        ## num 이하인 애들은 탐색 불가

        for next in List:
            time, wage,num = next
            if  d > num:
                continue
            else:
                ans += wage
                dfs(next,num+1+time)
                ans -= wage
        ansList.append(ans)
    return
for i,a in enumerate(List):
    a.append(i)
for a in List:
    ## 첫번째 일정부터 쭉 넣어서 계산 이떄 넣고 다시 마지막 백트래킹을 해줘야닿ㅁ
    ## 이런구조로짜면 처음 넣는 값은 여기서 처리해 줘야 될거임
    ## 깊이를 넣어야 되겠음
    ## 걸리는 시간, 임금, 숫자
    t,w,m = a
    ans += w
    dfs(a,t+m+1)
    ans -= w
print(max(ansList))

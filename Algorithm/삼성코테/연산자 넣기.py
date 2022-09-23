def dfs(start,last, cal):
    global ans
    ## 후보 선택할떄 가능한 애들 다 선정
    calculateCopy[cal] -= 1
    S = start
    L = List[last]
    # start 는 이전 단계의 ans
    if cal == 0:
        ans = S + L
    elif cal == 1:
        ans = S -L
    elif cal == 2:
        ans = S * L
    elif cal == 3:
        if S >= 0 :
            if L < 0:
                ans = S // abs(L) * -1
            else:
                ans = S //L
        else:
            if L < 0:
                ans = abs(S) // abs(L)
            else:
                ans = abs(S) //L
    for k in range(4):
        # 선택가능하고
        if calculateCopy[k] > 0:
            if last+1 <= len(List):
                dfs(ans,last+1,k)
                ##종료돼서 돌아오면
    if max(calculateCopy) == 0:
        ansList.append(ans)
    ## 복구 연산자 복구, ans 복구
    calculateCopy[cal] += 1
    if cal == 0:
        ans = ans - L
    elif cal == 1:
        ans = ans + L
    elif cal == 2:
        ans = ans // L
    elif cal == 3:
        if ans >= 0 :
            if L < 0:
                ans = S
            else:
                ans = S
        else:
            if L < 0:
                ans = S
            else:
                ans = S
        ## 이전단계
        ## 다 선택불가능이라 빠꾸먹으면 종료
N = int(input())
List = list(map(int,input().split()))
ansList = []
ans = 0
# 덧뺄곱나

calculate = list(map(int,input().split()))
for i in range(4):
    calculateCopy = calculate.copy()
    if calculateCopy[i] > 0:
        dfs(List[0],1,i)
    ans = 0

print(max(ansList))
print(min(ansList))
ansList = []
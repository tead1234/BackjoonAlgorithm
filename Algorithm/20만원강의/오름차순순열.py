li = list(map(int, input().split()))
N = li[0]
M = li[1]
k = 0
checked = [False] * (N)
answer = []
def dfs(N, M, o):
    global k
    global answer
    global checked
    ## dfs 탈출조건
    ## 반복루프
    ### 백트래킹
    if o == M:
        for a in answer:
            print(a, end= " ")
        print()
        return
    if o < M:
        for i in range(N):
            if checked[i] == False:
                checked[i] = True
                if len(answer) == 0 or answer[o-1] < i+1:
                    answer.append(i + 1)
                    dfs(N, M, o+1)
                    answer.pop()
                checked[i]= False

            if checked[i]:
                continue
dfs(N,M,0)








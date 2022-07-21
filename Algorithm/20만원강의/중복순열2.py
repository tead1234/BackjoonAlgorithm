li = list(map(int, input().split()))
N = li[0]
M = li[1]
k = 0
checked = [False] * N
answer = []


def dfs(N, M, o):
    global k
    global answer
    global checked
    if o == M:
        for i in answer:
            print(i, end=" ")
        print()
        return
    if o < M:
        for i in range(N):
            if checked[i]:
                continue
            answer.append(i+1)
            dfs(N,M,o+1)
            answer.pop()
            checked[i] = False
dfs(N,M,0)








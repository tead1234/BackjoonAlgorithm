def solution(n, lighthouse):
    vis = [False] * n
    lList = [0] * (n + 1)
    k = 0
    answer  = 0
    g = [[] for i in range(n + 1)]
    for a in lighthouse:
        x, y = a
        g[x].append(y)
        g[y].append(x)
    for b in g:
        L = len(b)
        lList[k] = L
        k += 1
    while False in vis:
        X = lList.index(max(lList))
        vis[lList.index(max(lList))-1] = True
        lList[lList.index(max(lList))] = 0
        for i in g[X]:
            vis[i-1] = True
            lList[i] -= 1

        answer += 1

    return answer

print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
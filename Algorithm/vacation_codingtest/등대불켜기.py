import heapq
def solution(n, lighthouse):
    vis = [False] * n
    lenghList = [0] * (n+1)
    finded = [0] * (n+1)
    k = 0
    answer  = 0
    g = [[] for _ in range(n + 1)]
    for a in lighthouse:
        x, y = a
        g[x].append(y)
        g[y].append(x)

    for b in g:
        L = len(b)
        lenghList[k] = L
        k += 1

    # print(g)
    # print(lenghList)
    ## 우선순위를 뽑을때 꼬리값을 기준으로 정렬해야됨
    ## 종점갯수로 정렬해서 배열에 넣어야 되는데
    q = []
    first = lenghList.index(max(lenghList))
    vis[first-1] = True
    answer += 1
    for c in g[first]:
        heapq.heappush(q,(-lenghList[c],c))
        finded[c] = 1
    while q:
        종점갯수,X = heapq.heappop(q)
        if vis[X-1] == True:
            continue
        else:
            ## X에서 갈수 있는 지점들중
            vis[X-1] = True
            for y in g[X]:
                if vis[y-1]:
                    continue
                else:
                    U = lenghList[y]
                    heapq.heappush(q, (-U,y))
                    if finded[y] == 0:
                        finded[y] = 1
                        for i in g[y]:
                            finded[i] = 1
                        answer += 1


    return answer

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
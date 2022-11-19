import heapq


def bfs(a, b):
    map = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]

    ]
    return map[a][b]


def findall(q, number):
    # global dist
    q2 = []
    dic = {

    }
    # q.sort()
    while q:
        W, L, R  = q.pop()
        next = int(number)

        A_next = bfs(L, next)
        B_next = bfs(R, next)
        ## 어차피 왼손 오른손 이 교환돼도 가중치는 같다
        ## left first
        if next != R:
            if next > R:
                temp = (R, next)
                if temp not in dic:
                    dic[temp] = W + A_next
                else:
                    if dic[temp] > W + A_next:
                        dic[temp] = W + A_next


            else:
                temp = (next,R)
                if temp not in dic:
                    dic[temp] = W + A_next
                else:
                    if dic[temp] > W + A_next:
                        dic[temp] = W + A_next

        #right
        if next != L:
            if next > L:
                temp = (L, next)
                if temp not in dic:
                    dic[temp] = W + B_next
                else:
                    if dic[temp] > W + B_next:
                        dic[temp] = W + B_next
            else:
                temp = (next,L)
                if temp not in dic:
                    dic[temp] = W + B_next
                else:
                    if dic[temp] > W + B_next:
                        dic[temp] = W + B_next

    for item in dic.items():
        points, val = item
        i,j = points
        heapq.heappush(q2,(val,i,j))


    return q2


def solution(numbers):

    q = []
    number = list(numbers)

    tar = int(number[0])
    del number[0]
    A = bfs(4, tar)
    B = bfs(6, tar)

    q.append((A, tar, 6))
    q.append((B, 4, tar))
    for n in number:
        q = findall(q, int(n))
        print(q)

    return q[0][0]


print(solution("0098"))

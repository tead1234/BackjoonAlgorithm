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
        [3, 6, 5, 4, 5, 3, 2, 4, 3, 1]
    ]
    return map[a][b]


def findall(q, number):
    q2 = []
    while q:
        W,L, R  = q.pop()
        next = int(number)

        A_next = bfs(L, next)
        B_next = bfs(R, next)
        if next == L:
            heapq.heappush(q2, (1 + W, next, R))
        elif next == R:
            heapq.heappush(q2, (1 + W, L, next))
        else:
            heapq.heappush(q2, (A_next + W, next, R))
            heapq.heappush(q2, (B_next + W, L, next))

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


    return q[0][0]


# print(solution("1756"))
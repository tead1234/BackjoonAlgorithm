import heapq
q = []
n = int(input())

for i in range(n):
    s = int(input())

    if s == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, s)


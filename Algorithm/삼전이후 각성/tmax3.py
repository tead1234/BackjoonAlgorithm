def solution(x, y, n):
    answer = 0
    d = [[] for _ in range(20)]
    # dp??
    if x == y:
        return 0
    d[0] = []
    d[1] = list(set([x + n, x * 2, x * 3]))
    if y in d[1]:
        return 1
    for i in range(2, 20):
        if len(d[i - 1]) == 0:
            return -1
        d[i] = set(d[i])
        for c in d[i - 1]:
            if y in [c + n, c * 3, c * 2]:
                return i

            if c + n < y:
                d[i].append(c + n)
            if c * 3 < y:
                d[i].append(c * 3)
            if c * 2 < y:
                d[i].append(c * 2)
        d[i] = list(d[i])

print(solution(10,150,4))
N = int(input())
M = int(input())
listD = list(map(int, input().split()))
max_val  = sorted(listD, reverse=True)[0]
res = 0
first = 0
last = max_val
while last > first:
    mid = (first + last)//2
    res = 0
    for a in listD:
        if a- mid > 0:
            res += (a - mid)
    if res == M:
        print(mid)
        break
    elif res > M:
        first = mid
    elif res < M:
        last = mid